#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SkuCreateInfoParam(object):

    def __init__(self):
        self._price = None
        self._shelf_code = None
        self._sku_code = None
        self._stock = None
        self._upc = None
        self._volume_high = None
        self._volume_length = None
        self._volume_width = None
        self._weight = None
        self._weight_unit = None

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def shelf_code(self):
        return self._shelf_code

    @shelf_code.setter
    def shelf_code(self, value):
        self._shelf_code = value
    @property
    def sku_code(self):
        return self._sku_code

    @sku_code.setter
    def sku_code(self, value):
        self._sku_code = value
    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        self._stock = value
    @property
    def upc(self):
        return self._upc

    @upc.setter
    def upc(self, value):
        self._upc = value
    @property
    def volume_high(self):
        return self._volume_high

    @volume_high.setter
    def volume_high(self, value):
        self._volume_high = value
    @property
    def volume_length(self):
        return self._volume_length

    @volume_length.setter
    def volume_length(self, value):
        self._volume_length = value
    @property
    def volume_width(self):
        return self._volume_width

    @volume_width.setter
    def volume_width(self, value):
        self._volume_width = value
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value
    @property
    def weight_unit(self):
        return self._weight_unit

    @weight_unit.setter
    def weight_unit(self, value):
        self._weight_unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.shelf_code:
            if hasattr(self.shelf_code, 'to_alipay_dict'):
                params['shelf_code'] = self.shelf_code.to_alipay_dict()
            else:
                params['shelf_code'] = self.shelf_code
        if self.sku_code:
            if hasattr(self.sku_code, 'to_alipay_dict'):
                params['sku_code'] = self.sku_code.to_alipay_dict()
            else:
                params['sku_code'] = self.sku_code
        if self.stock:
            if hasattr(self.stock, 'to_alipay_dict'):
                params['stock'] = self.stock.to_alipay_dict()
            else:
                params['stock'] = self.stock
        if self.upc:
            if hasattr(self.upc, 'to_alipay_dict'):
                params['upc'] = self.upc.to_alipay_dict()
            else:
                params['upc'] = self.upc
        if self.volume_high:
            if hasattr(self.volume_high, 'to_alipay_dict'):
                params['volume_high'] = self.volume_high.to_alipay_dict()
            else:
                params['volume_high'] = self.volume_high
        if self.volume_length:
            if hasattr(self.volume_length, 'to_alipay_dict'):
                params['volume_length'] = self.volume_length.to_alipay_dict()
            else:
                params['volume_length'] = self.volume_length
        if self.volume_width:
            if hasattr(self.volume_width, 'to_alipay_dict'):
                params['volume_width'] = self.volume_width.to_alipay_dict()
            else:
                params['volume_width'] = self.volume_width
        if self.weight:
            if hasattr(self.weight, 'to_alipay_dict'):
                params['weight'] = self.weight.to_alipay_dict()
            else:
                params['weight'] = self.weight
        if self.weight_unit:
            if hasattr(self.weight_unit, 'to_alipay_dict'):
                params['weight_unit'] = self.weight_unit.to_alipay_dict()
            else:
                params['weight_unit'] = self.weight_unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SkuCreateInfoParam()
        if 'price' in d:
            o.price = d['price']
        if 'shelf_code' in d:
            o.shelf_code = d['shelf_code']
        if 'sku_code' in d:
            o.sku_code = d['sku_code']
        if 'stock' in d:
            o.stock = d['stock']
        if 'upc' in d:
            o.upc = d['upc']
        if 'volume_high' in d:
            o.volume_high = d['volume_high']
        if 'volume_length' in d:
            o.volume_length = d['volume_length']
        if 'volume_width' in d:
            o.volume_width = d['volume_width']
        if 'weight' in d:
            o.weight = d['weight']
        if 'weight_unit' in d:
            o.weight_unit = d['weight_unit']
        return o


