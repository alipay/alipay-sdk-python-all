#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CardTemplateInfo import CardTemplateInfo


class AlipayCommerceCardTemplateCreateModel(object):

    def __init__(self):
        self._card_template_info = None

    @property
    def card_template_info(self):
        return self._card_template_info

    @card_template_info.setter
    def card_template_info(self, value):
        if isinstance(value, CardTemplateInfo):
            self._card_template_info = value
        else:
            self._card_template_info = CardTemplateInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.card_template_info:
            if hasattr(self.card_template_info, 'to_alipay_dict'):
                params['card_template_info'] = self.card_template_info.to_alipay_dict()
            else:
                params['card_template_info'] = self.card_template_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCardTemplateCreateModel()
        if 'card_template_info' in d:
            o.card_template_info = d['card_template_info']
        return o


