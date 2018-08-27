#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExchangeRate(object):

    def __init__(self):
        self._base_currency = None
        self._exchange_currency = None
        self._rate = None

    @property
    def base_currency(self):
        return self._base_currency

    @base_currency.setter
    def base_currency(self, value):
        self._base_currency = value
    @property
    def exchange_currency(self):
        return self._exchange_currency

    @exchange_currency.setter
    def exchange_currency(self, value):
        self._exchange_currency = value
    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        self._rate = value


    def to_alipay_dict(self):
        params = dict()
        if self.base_currency:
            if hasattr(self.base_currency, 'to_alipay_dict'):
                params['base_currency'] = self.base_currency.to_alipay_dict()
            else:
                params['base_currency'] = self.base_currency
        if self.exchange_currency:
            if hasattr(self.exchange_currency, 'to_alipay_dict'):
                params['exchange_currency'] = self.exchange_currency.to_alipay_dict()
            else:
                params['exchange_currency'] = self.exchange_currency
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
        o = ExchangeRate()
        if 'base_currency' in d:
            o.base_currency = d['base_currency']
        if 'exchange_currency' in d:
            o.exchange_currency = d['exchange_currency']
        if 'rate' in d:
            o.rate = d['rate']
        return o


