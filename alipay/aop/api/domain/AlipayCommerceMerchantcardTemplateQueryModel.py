#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMerchantcardTemplateQueryModel(object):

    def __init__(self):
        self._card_template_id = None

    @property
    def card_template_id(self):
        return self._card_template_id

    @card_template_id.setter
    def card_template_id(self, value):
        self._card_template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_template_id:
            if hasattr(self.card_template_id, 'to_alipay_dict'):
                params['card_template_id'] = self.card_template_id.to_alipay_dict()
            else:
                params['card_template_id'] = self.card_template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMerchantcardTemplateQueryModel()
        if 'card_template_id' in d:
            o.card_template_id = d['card_template_id']
        return o


