#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ShiftStockVO import ShiftStockVO


class SkuStockInfo(object):

    def __init__(self):
        self._shift_stock_list = None
        self._sku_code = None

    @property
    def shift_stock_list(self):
        return self._shift_stock_list

    @shift_stock_list.setter
    def shift_stock_list(self, value):
        if isinstance(value, list):
            self._shift_stock_list = list()
            for i in value:
                if isinstance(i, ShiftStockVO):
                    self._shift_stock_list.append(i)
                else:
                    self._shift_stock_list.append(ShiftStockVO.from_alipay_dict(i))
    @property
    def sku_code(self):
        return self._sku_code

    @sku_code.setter
    def sku_code(self, value):
        self._sku_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.shift_stock_list:
            if isinstance(self.shift_stock_list, list):
                for i in range(0, len(self.shift_stock_list)):
                    element = self.shift_stock_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shift_stock_list[i] = element.to_alipay_dict()
            if hasattr(self.shift_stock_list, 'to_alipay_dict'):
                params['shift_stock_list'] = self.shift_stock_list.to_alipay_dict()
            else:
                params['shift_stock_list'] = self.shift_stock_list
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
        o = SkuStockInfo()
        if 'shift_stock_list' in d:
            o.shift_stock_list = d['shift_stock_list']
        if 'sku_code' in d:
            o.sku_code = d['sku_code']
        return o


