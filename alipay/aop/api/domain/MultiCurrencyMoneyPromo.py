#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MultiCurrencyMoneyPromo(object):

    def __init__(self):
        self._cent = None
        self._currency = None

    @property
    def cent(self):
        return self._cent

    @cent.setter
    def cent(self, value):
        self._cent = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value


    def to_alipay_dict(self):
        params = dict()
        if self.cent:
            if hasattr(self.cent, 'to_alipay_dict'):
                params['cent'] = self.cent.to_alipay_dict()
            else:
                params['cent'] = self.cent
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MultiCurrencyMoneyPromo()
        if 'cent' in d:
            o.cent = d['cent']
        if 'currency' in d:
            o.currency = d['currency']
        return o


