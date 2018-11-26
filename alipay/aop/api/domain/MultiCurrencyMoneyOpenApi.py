#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MultiCurrencyMoneyOpenApi(object):

    def __init__(self):
        self._cent = None
        self._currency_value = None

    @property
    def cent(self):
        return self._cent

    @cent.setter
    def cent(self, value):
        self._cent = value
    @property
    def currency_value(self):
        return self._currency_value

    @currency_value.setter
    def currency_value(self, value):
        self._currency_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.cent:
            if hasattr(self.cent, 'to_alipay_dict'):
                params['cent'] = self.cent.to_alipay_dict()
            else:
                params['cent'] = self.cent
        if self.currency_value:
            if hasattr(self.currency_value, 'to_alipay_dict'):
                params['currency_value'] = self.currency_value.to_alipay_dict()
            else:
                params['currency_value'] = self.currency_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MultiCurrencyMoneyOpenApi()
        if 'cent' in d:
            o.cent = d['cent']
        if 'currency_value' in d:
            o.currency_value = d['currency_value']
        return o


