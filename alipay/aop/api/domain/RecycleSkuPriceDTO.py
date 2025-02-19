#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleSkuPriceDTO(object):

    def __init__(self):
        self._max_price = None
        self._min_price = None

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


    def to_alipay_dict(self):
        params = dict()
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleSkuPriceDTO()
        if 'max_price' in d:
            o.max_price = d['max_price']
        if 'min_price' in d:
            o.min_price = d['min_price']
        return o


