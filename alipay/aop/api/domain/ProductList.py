#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ProductList(object):

    def __init__(self):
        self._discount_price = None
        self._listed_price = None
        self._price_unit = None
        self._sku_code = None

    @property
    def discount_price(self):
        return self._discount_price

    @discount_price.setter
    def discount_price(self, value):
        self._discount_price = value
    @property
    def listed_price(self):
        return self._listed_price

    @listed_price.setter
    def listed_price(self, value):
        self._listed_price = value
    @property
    def price_unit(self):
        return self._price_unit

    @price_unit.setter
    def price_unit(self, value):
        self._price_unit = value
    @property
    def sku_code(self):
        return self._sku_code

    @sku_code.setter
    def sku_code(self, value):
        self._sku_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.discount_price:
            if hasattr(self.discount_price, 'to_alipay_dict'):
                params['discount_price'] = self.discount_price.to_alipay_dict()
            else:
                params['discount_price'] = self.discount_price
        if self.listed_price:
            if hasattr(self.listed_price, 'to_alipay_dict'):
                params['listed_price'] = self.listed_price.to_alipay_dict()
            else:
                params['listed_price'] = self.listed_price
        if self.price_unit:
            if hasattr(self.price_unit, 'to_alipay_dict'):
                params['price_unit'] = self.price_unit.to_alipay_dict()
            else:
                params['price_unit'] = self.price_unit
        if self.sku_code:
            if hasattr(self.sku_code, 'to_alipay_dict'):
                params['sku_code'] = self.sku_code.to_alipay_dict()
            else:
                params['sku_code'] = self.sku_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProductList()
        if 'discount_price' in d:
            o.discount_price = d['discount_price']
        if 'listed_price' in d:
            o.listed_price = d['listed_price']
        if 'price_unit' in d:
            o.price_unit = d['price_unit']
        if 'sku_code' in d:
            o.sku_code = d['sku_code']
        return o


