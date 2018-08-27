#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingMallTradeSubscribeModel(object):

    def __init__(self):
        self._card_template_id = None
        self._mall_id = None

    @property
    def card_template_id(self):
        return self._card_template_id

    @card_template_id.setter
    def card_template_id(self, value):
        self._card_template_id = value
    @property
    def mall_id(self):
        return self._mall_id

    @mall_id.setter
    def mall_id(self, value):
        self._mall_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_template_id:
            if hasattr(self.card_template_id, 'to_alipay_dict'):
                params['card_template_id'] = self.card_template_id.to_alipay_dict()
            else:
                params['card_template_id'] = self.card_template_id
        if self.mall_id:
            if hasattr(self.mall_id, 'to_alipay_dict'):
                params['mall_id'] = self.mall_id.to_alipay_dict()
            else:
                params['mall_id'] = self.mall_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingMallTradeSubscribeModel()
        if 'card_template_id' in d:
            o.card_template_id = d['card_template_id']
        if 'mall_id' in d:
            o.mall_id = d['mall_id']
        return o


