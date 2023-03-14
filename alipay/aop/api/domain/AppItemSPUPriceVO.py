#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AppItemSPUPriceVO(object):

    def __init__(self):
        self._has_price = None
        self._original_price = None
        self._original_price_max = None
        self._original_price_min = None
        self._price = None
        self._price_max = None
        self._price_min = None
        self._price_unit = None

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
    def original_price_max(self):
        return self._original_price_max

    @original_price_max.setter
    def original_price_max(self, value):
        self._original_price_max = value
    @property
    def original_price_min(self):
        return self._original_price_min

    @original_price_min.setter
    def original_price_min(self, value):
        self._original_price_min = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def price_max(self):
        return self._price_max

    @price_max.setter
    def price_max(self, value):
        self._price_max = value
    @property
    def price_min(self):
        return self._price_min

    @price_min.setter
    def price_min(self, value):
        self._price_min = value
    @property
    def price_unit(self):
        return self._price_unit

    @price_unit.setter
    def price_unit(self, value):
        self._price_unit = value


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
        if self.original_price_max:
            if hasattr(self.original_price_max, 'to_alipay_dict'):
                params['original_price_max'] = self.original_price_max.to_alipay_dict()
            else:
                params['original_price_max'] = self.original_price_max
        if self.original_price_min:
            if hasattr(self.original_price_min, 'to_alipay_dict'):
                params['original_price_min'] = self.original_price_min.to_alipay_dict()
            else:
                params['original_price_min'] = self.original_price_min
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.price_max:
            if hasattr(self.price_max, 'to_alipay_dict'):
                params['price_max'] = self.price_max.to_alipay_dict()
            else:
                params['price_max'] = self.price_max
        if self.price_min:
            if hasattr(self.price_min, 'to_alipay_dict'):
                params['price_min'] = self.price_min.to_alipay_dict()
            else:
                params['price_min'] = self.price_min
        if self.price_unit:
            if hasattr(self.price_unit, 'to_alipay_dict'):
                params['price_unit'] = self.price_unit.to_alipay_dict()
            else:
                params['price_unit'] = self.price_unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AppItemSPUPriceVO()
        if 'has_price' in d:
            o.has_price = d['has_price']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'original_price_max' in d:
            o.original_price_max = d['original_price_max']
        if 'original_price_min' in d:
            o.original_price_min = d['original_price_min']
        if 'price' in d:
            o.price = d['price']
        if 'price_max' in d:
            o.price_max = d['price_max']
        if 'price_min' in d:
            o.price_min = d['price_min']
        if 'price_unit' in d:
            o.price_unit = d['price_unit']
        return o


