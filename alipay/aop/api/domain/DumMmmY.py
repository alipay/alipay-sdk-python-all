#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DumMmmY(object):

    def __init__(self):
        self._price = None

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value


    def to_alipay_dict(self):
        params = dict()
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
        o = DumMmmY()
        if 'price' in d:
            o.price = d['price']
        return o


