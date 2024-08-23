#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantPriceRelInfo(object):

    def __init__(self):
        self._back_product_code = None
        self._price_rate = None

    @property
    def back_product_code(self):
        return self._back_product_code

    @back_product_code.setter
    def back_product_code(self, value):
        self._back_product_code = value
    @property
    def price_rate(self):
        return self._price_rate

    @price_rate.setter
    def price_rate(self, value):
        self._price_rate = value


    def to_alipay_dict(self):
        params = dict()
        if self.back_product_code:
            if hasattr(self.back_product_code, 'to_alipay_dict'):
                params['back_product_code'] = self.back_product_code.to_alipay_dict()
            else:
                params['back_product_code'] = self.back_product_code
        if self.price_rate:
            if hasattr(self.price_rate, 'to_alipay_dict'):
                params['price_rate'] = self.price_rate.to_alipay_dict()
            else:
                params['price_rate'] = self.price_rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantPriceRelInfo()
        if 'back_product_code' in d:
            o.back_product_code = d['back_product_code']
        if 'price_rate' in d:
            o.price_rate = d['price_rate']
        return o


