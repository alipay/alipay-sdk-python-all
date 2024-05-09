#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LocalItemDirectModifySku(object):

    def __init__(self):
        self._limit_type = None
        self._original_price = None
        self._out_sku_id = None
        self._sale_price = None
        self._sale_status = None
        self._sku_id = None
        self._stock_limit_type = None
        self._stock_num = None

    @property
    def limit_type(self):
        return self._limit_type

    @limit_type.setter
    def limit_type(self, value):
        self._limit_type = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def out_sku_id(self):
        return self._out_sku_id

    @out_sku_id.setter
    def out_sku_id(self, value):
        self._out_sku_id = value
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value
    @property
    def sale_status(self):
        return self._sale_status

    @sale_status.setter
    def sale_status(self, value):
        self._sale_status = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def stock_limit_type(self):
        return self._stock_limit_type

    @stock_limit_type.setter
    def stock_limit_type(self, value):
        self._stock_limit_type = value
    @property
    def stock_num(self):
        return self._stock_num

    @stock_num.setter
    def stock_num(self, value):
        self._stock_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.limit_type:
            if hasattr(self.limit_type, 'to_alipay_dict'):
                params['limit_type'] = self.limit_type.to_alipay_dict()
            else:
                params['limit_type'] = self.limit_type
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.out_sku_id:
            if hasattr(self.out_sku_id, 'to_alipay_dict'):
                params['out_sku_id'] = self.out_sku_id.to_alipay_dict()
            else:
                params['out_sku_id'] = self.out_sku_id
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
        if self.sale_status:
            if hasattr(self.sale_status, 'to_alipay_dict'):
                params['sale_status'] = self.sale_status.to_alipay_dict()
            else:
                params['sale_status'] = self.sale_status
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.stock_limit_type:
            if hasattr(self.stock_limit_type, 'to_alipay_dict'):
                params['stock_limit_type'] = self.stock_limit_type.to_alipay_dict()
            else:
                params['stock_limit_type'] = self.stock_limit_type
        if self.stock_num:
            if hasattr(self.stock_num, 'to_alipay_dict'):
                params['stock_num'] = self.stock_num.to_alipay_dict()
            else:
                params['stock_num'] = self.stock_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LocalItemDirectModifySku()
        if 'limit_type' in d:
            o.limit_type = d['limit_type']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'out_sku_id' in d:
            o.out_sku_id = d['out_sku_id']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        if 'sale_status' in d:
            o.sale_status = d['sale_status']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'stock_limit_type' in d:
            o.stock_limit_type = d['stock_limit_type']
        if 'stock_num' in d:
            o.stock_num = d['stock_num']
        return o


