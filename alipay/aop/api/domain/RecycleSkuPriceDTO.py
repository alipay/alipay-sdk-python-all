#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecyclePriceExtDTO import RecyclePriceExtDTO
from alipay.aop.api.domain.RecycleSkuPriceExtDTO import RecycleSkuPriceExtDTO


class RecycleSkuPriceDTO(object):

    def __init__(self):
        self._max_price = None
        self._min_price = None
        self._price_ext = None
        self._price_extend = None
        self._sale_price = None
        self._sku_price_type = None

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
    @property
    def price_ext(self):
        return self._price_ext

    @price_ext.setter
    def price_ext(self, value):
        if isinstance(value, list):
            self._price_ext = list()
            for i in value:
                if isinstance(i, RecyclePriceExtDTO):
                    self._price_ext.append(i)
                else:
                    self._price_ext.append(RecyclePriceExtDTO.from_alipay_dict(i))
    @property
    def price_extend(self):
        return self._price_extend

    @price_extend.setter
    def price_extend(self, value):
        if isinstance(value, RecycleSkuPriceExtDTO):
            self._price_extend = value
        else:
            self._price_extend = RecycleSkuPriceExtDTO.from_alipay_dict(value)
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value
    @property
    def sku_price_type(self):
        return self._sku_price_type

    @sku_price_type.setter
    def sku_price_type(self, value):
        self._sku_price_type = value


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
        if self.price_ext:
            if isinstance(self.price_ext, list):
                for i in range(0, len(self.price_ext)):
                    element = self.price_ext[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.price_ext[i] = element.to_alipay_dict()
            if hasattr(self.price_ext, 'to_alipay_dict'):
                params['price_ext'] = self.price_ext.to_alipay_dict()
            else:
                params['price_ext'] = self.price_ext
        if self.price_extend:
            if hasattr(self.price_extend, 'to_alipay_dict'):
                params['price_extend'] = self.price_extend.to_alipay_dict()
            else:
                params['price_extend'] = self.price_extend
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
        if self.sku_price_type:
            if hasattr(self.sku_price_type, 'to_alipay_dict'):
                params['sku_price_type'] = self.sku_price_type.to_alipay_dict()
            else:
                params['sku_price_type'] = self.sku_price_type
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
        if 'price_ext' in d:
            o.price_ext = d['price_ext']
        if 'price_extend' in d:
            o.price_extend = d['price_extend']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        if 'sku_price_type' in d:
            o.sku_price_type = d['sku_price_type']
        return o


