#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecommendPrice(object):

    def __init__(self):
        self._freq = None
        self._is_suggest_price = None
        self._price = None

    @property
    def freq(self):
        return self._freq

    @freq.setter
    def freq(self, value):
        self._freq = value
    @property
    def is_suggest_price(self):
        return self._is_suggest_price

    @is_suggest_price.setter
    def is_suggest_price(self, value):
        self._is_suggest_price = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value


    def to_alipay_dict(self):
        params = dict()
        if self.freq:
            if hasattr(self.freq, 'to_alipay_dict'):
                params['freq'] = self.freq.to_alipay_dict()
            else:
                params['freq'] = self.freq
        if self.is_suggest_price:
            if hasattr(self.is_suggest_price, 'to_alipay_dict'):
                params['is_suggest_price'] = self.is_suggest_price.to_alipay_dict()
            else:
                params['is_suggest_price'] = self.is_suggest_price
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecommendPrice()
        if 'freq' in d:
            o.freq = d['freq']
        if 'is_suggest_price' in d:
            o.is_suggest_price = d['is_suggest_price']
        if 'price' in d:
            o.price = d['price']
        return o


