#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MultiCurrencyMoney(object):

    def __init__(self):
        self._amt = None
        self._currency_code = None

    @property
    def amt(self):
        return self._amt

    @amt.setter
    def amt(self, value):
        self._amt = value
    @property
    def currency_code(self):
        return self._currency_code

    @currency_code.setter
    def currency_code(self, value):
        self._currency_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.amt:
            if hasattr(self.amt, 'to_alipay_dict'):
                params['amt'] = self.amt.to_alipay_dict()
            else:
                params['amt'] = self.amt
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
        o = MultiCurrencyMoney()
        if 'amt' in d:
            o.amt = d['amt']
        if 'currency_code' in d:
            o.currency_code = d['currency_code']
        return o


