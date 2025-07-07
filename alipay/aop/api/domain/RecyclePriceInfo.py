#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecyclePriceInfo(object):

    def __init__(self):
        self._assess_amount = None
        self._max_price = None
        self._min_price = None
        self._price_code = None

    @property
    def assess_amount(self):
        return self._assess_amount

    @assess_amount.setter
    def assess_amount(self, value):
        self._assess_amount = value
    @property
    def max_price(self):
        return self._max_price

    @max_price.setter
    def max_price(self, value):
        self._max_price = value
    @property
    def min_price(self):
        return self._min_price

    @min_price.setter
    def min_price(self, value):
        self._min_price = value
    @property
    def price_code(self):
        return self._price_code

    @price_code.setter
    def price_code(self, value):
        self._price_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.assess_amount:
            if hasattr(self.assess_amount, 'to_alipay_dict'):
                params['assess_amount'] = self.assess_amount.to_alipay_dict()
            else:
                params['assess_amount'] = self.assess_amount
        if self.max_price:
            if hasattr(self.max_price, 'to_alipay_dict'):
                params['max_price'] = self.max_price.to_alipay_dict()
            else:
                params['max_price'] = self.max_price
        if self.min_price:
            if hasattr(self.min_price, 'to_alipay_dict'):
                params['min_price'] = self.min_price.to_alipay_dict()
            else:
                params['min_price'] = self.min_price
        if self.price_code:
            if hasattr(self.price_code, 'to_alipay_dict'):
                params['price_code'] = self.price_code.to_alipay_dict()
            else:
                params['price_code'] = self.price_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecyclePriceInfo()
        if 'assess_amount' in d:
            o.assess_amount = d['assess_amount']
        if 'max_price' in d:
            o.max_price = d['max_price']
        if 'min_price' in d:
            o.min_price = d['min_price']
        if 'price_code' in d:
            o.price_code = d['price_code']
        return o


