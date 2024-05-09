#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantCardTemplate import MerchantCardTemplate


class AlipayCommerceMerchantcardTemplateCreateModel(object):

    def __init__(self):
        self._card_template = None

    @property
    def card_template(self):
        return self._card_template

    @card_template.setter
    def card_template(self, value):
        if isinstance(value, MerchantCardTemplate):
            self._card_template = value
        else:
            self._card_template = MerchantCardTemplate.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.card_template:
            if hasattr(self.card_template, 'to_alipay_dict'):
                params['card_template'] = self.card_template.to_alipay_dict()
            else:
                params['card_template'] = self.card_template
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMerchantcardTemplateCreateModel()
        if 'card_template' in d:
            o.card_template = d['card_template']
        return o


