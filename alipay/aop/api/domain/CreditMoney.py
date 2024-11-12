#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreditMoney(object):

    def __init__(self):
        self._cent = None
        self._currency_code = None

    @property
    def cent(self):
        return self._cent

    @cent.setter
    def cent(self, value):
        self._cent = value
    @property
    def currency_code(self):
        return self._currency_code

    @currency_code.setter
    def currency_code(self, value):
        self._currency_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.cent:
            if hasattr(self.cent, 'to_alipay_dict'):
                params['cent'] = self.cent.to_alipay_dict()
            else:
                params['cent'] = self.cent
        if self.currency_code:
            if hasattr(self.currency_code, 'to_alipay_dict'):
                params['currency_code'] = self.currency_code.to_alipay_dict()
            else:
                params['currency_code'] = self.currency_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditMoney()
        if 'cent' in d:
            o.cent = d['cent']
        if 'currency_code' in d:
            o.currency_code = d['currency_code']
        return o


