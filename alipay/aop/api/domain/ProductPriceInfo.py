#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ProductPriceInfo(object):

    def __init__(self):
        self._price_rate = None
        self._product_detail_code = None

    @property
    def price_rate(self):
        return self._price_rate

    @price_rate.setter
    def price_rate(self, value):
        self._price_rate = value
    @property
    def product_detail_code(self):
        return self._product_detail_code

    @product_detail_code.setter
    def product_detail_code(self, value):
        self._product_detail_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.price_rate:
            if hasattr(self.price_rate, 'to_alipay_dict'):
                params['price_rate'] = self.price_rate.to_alipay_dict()
            else:
                params['price_rate'] = self.price_rate
        if self.product_detail_code:
            if hasattr(self.product_detail_code, 'to_alipay_dict'):
                params['product_detail_code'] = self.product_detail_code.to_alipay_dict()
            else:
                params['product_detail_code'] = self.product_detail_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProductPriceInfo()
        if 'price_rate' in d:
            o.price_rate = d['price_rate']
        if 'product_detail_code' in d:
            o.product_detail_code = d['product_detail_code']
        return o


