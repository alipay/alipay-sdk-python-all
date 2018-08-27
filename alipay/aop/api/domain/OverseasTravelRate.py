#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OverseasTravelRate(object):

    def __init__(self):
        self._currency = None
        self._currency_icon = None
        self._rate = None

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def currency_icon(self):
        return self._currency_icon

    @currency_icon.setter
    def currency_icon(self, value):
        self._currency_icon = value
    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        self._rate = value


    def to_alipay_dict(self):
        params = dict()
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.currency_icon:
            if hasattr(self.currency_icon, 'to_alipay_dict'):
                params['currency_icon'] = self.currency_icon.to_alipay_dict()
            else:
                params['currency_icon'] = self.currency_icon
        if self.rate:
            if hasattr(self.rate, 'to_alipay_dict'):
                params['rate'] = self.rate.to_alipay_dict()
            else:
                params['rate'] = self.rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OverseasTravelRate()
        if 'currency' in d:
            o.currency = d['currency']
        if 'currency_icon' in d:
            o.currency_icon = d['currency_icon']
        if 'rate' in d:
            o.rate = d['rate']
        return o


