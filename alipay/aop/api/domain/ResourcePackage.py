#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ResourcePackage(object):

    def __init__(self):
        self._currency = None
        self._name = None
        self._original_price = None
        self._spec_code = None
        self._time_unit = None
        self._trade_price = None

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def spec_code(self):
        return self._spec_code

    @spec_code.setter
    def spec_code(self, value):
        self._spec_code = value
    @property
    def time_unit(self):
        return self._time_unit

    @time_unit.setter
    def time_unit(self, value):
        self._time_unit = value
    @property
    def trade_price(self):
        return self._trade_price

    @trade_price.setter
    def trade_price(self, value):
        self._trade_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.spec_code:
            if hasattr(self.spec_code, 'to_alipay_dict'):
                params['spec_code'] = self.spec_code.to_alipay_dict()
            else:
                params['spec_code'] = self.spec_code
        if self.time_unit:
            if hasattr(self.time_unit, 'to_alipay_dict'):
                params['time_unit'] = self.time_unit.to_alipay_dict()
            else:
                params['time_unit'] = self.time_unit
        if self.trade_price:
            if hasattr(self.trade_price, 'to_alipay_dict'):
                params['trade_price'] = self.trade_price.to_alipay_dict()
            else:
                params['trade_price'] = self.trade_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ResourcePackage()
        if 'currency' in d:
            o.currency = d['currency']
        if 'name' in d:
            o.name = d['name']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'spec_code' in d:
            o.spec_code = d['spec_code']
        if 'time_unit' in d:
            o.time_unit = d['time_unit']
        if 'trade_price' in d:
            o.trade_price = d['trade_price']
        return o


