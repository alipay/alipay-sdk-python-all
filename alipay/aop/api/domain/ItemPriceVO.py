#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemPriceVO(object):

    def __init__(self):
        self._has_price = None
        self._original_price = None
        self._price_unit = None
        self._sale_price = None

    @property
    def has_price(self):
        return self._has_price

    @has_price.setter
    def has_price(self, value):
        self._has_price = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def price_unit(self):
        return self._price_unit

    @price_unit.setter
    def price_unit(self, value):
        self._price_unit = value
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.has_price:
            if hasattr(self.has_price, 'to_alipay_dict'):
                params['has_price'] = self.has_price.to_alipay_dict()
            else:
                params['has_price'] = self.has_price
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.price_unit:
            if hasattr(self.price_unit, 'to_alipay_dict'):
                params['price_unit'] = self.price_unit.to_alipay_dict()
            else:
                params['price_unit'] = self.price_unit
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemPriceVO()
        if 'has_price' in d:
            o.has_price = d['has_price']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'price_unit' in d:
            o.price_unit = d['price_unit']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        return o


