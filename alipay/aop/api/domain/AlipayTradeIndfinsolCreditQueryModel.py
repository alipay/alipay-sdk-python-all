#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeIndfinsolCreditQueryModel(object):

    def __init__(self):
        self._bank_card_token = None
        self._biz_type = None

    @property
    def bank_card_token(self):
        return self._bank_card_token

    @bank_card_token.setter
    def bank_card_token(self, value):
        self._bank_card_token = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_card_token:
            if hasattr(self.bank_card_token, 'to_alipay_dict'):
                params['bank_card_token'] = self.bank_card_token.to_alipay_dict()
            else:
                params['bank_card_token'] = self.bank_card_token
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeIndfinsolCreditQueryModel()
        if 'bank_card_token' in d:
            o.bank_card_token = d['bank_card_token']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        return o


