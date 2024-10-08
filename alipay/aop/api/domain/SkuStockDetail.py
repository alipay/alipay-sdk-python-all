#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SkuStockDetail(object):

    def __init__(self):
        self._sku_code = None
        self._stock = None

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


    def to_alipay_dict(self):
        params = dict()
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SkuStockDetail()
        if 'sku_code' in d:
            o.sku_code = d['sku_code']
        if 'stock' in d:
            o.stock = d['stock']
        return o


