#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BookPriceInfo(object):

    def __init__(self):
        self._price = None
        self._sell_type = None

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def sell_type(self):
        return self._sell_type

    @sell_type.setter
    def sell_type(self, value):
        self._sell_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.sell_type:
            if hasattr(self.sell_type, 'to_alipay_dict'):
                params['sell_type'] = self.sell_type.to_alipay_dict()
            else:
                params['sell_type'] = self.sell_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BookPriceInfo()
        if 'price' in d:
            o.price = d['price']
        if 'sell_type' in d:
            o.sell_type = d['sell_type']
        return o


