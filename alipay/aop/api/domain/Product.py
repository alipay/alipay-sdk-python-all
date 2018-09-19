#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Product(object):

    def __init__(self):
        self._name = None
        self._price = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value


    def to_alipay_dict(self):
        params = dict()
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
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
        o = Product()
        if 'name' in d:
            o.name = d['name']
        if 'price' in d:
            o.price = d['price']
        return o


