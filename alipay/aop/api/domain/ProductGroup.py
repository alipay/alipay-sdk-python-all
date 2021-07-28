#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ProductInfo import ProductInfo


class ProductGroup(object):

    def __init__(self):
        self._count = None
        self._product = None
        self._total_price = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        if isinstance(value, ProductInfo):
            self._product = value
        else:
            self._product = ProductInfo.from_alipay_dict(value)
    @property
    def total_price(self):
        return self._total_price

    @total_price.setter
    def total_price(self, value):
        self._total_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.product:
            if hasattr(self.product, 'to_alipay_dict'):
                params['product'] = self.product.to_alipay_dict()
            else:
                params['product'] = self.product
        if self.total_price:
            if hasattr(self.total_price, 'to_alipay_dict'):
                params['total_price'] = self.total_price.to_alipay_dict()
            else:
                params['total_price'] = self.total_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProductGroup()
        if 'count' in d:
            o.count = d['count']
        if 'product' in d:
            o.product = d['product']
        if 'total_price' in d:
            o.total_price = d['total_price']
        return o


