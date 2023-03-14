#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SpuStock(object):

    def __init__(self):
        self._available_stock_num = None
        self._stock_num = None
        self._withholding_stock_num = None

    @property
    def available_stock_num(self):
        return self._available_stock_num

    @available_stock_num.setter
    def available_stock_num(self, value):
        self._available_stock_num = value
    @property
    def stock_num(self):
        return self._stock_num

    @stock_num.setter
    def stock_num(self, value):
        self._stock_num = value
    @property
    def withholding_stock_num(self):
        return self._withholding_stock_num

    @withholding_stock_num.setter
    def withholding_stock_num(self, value):
        self._withholding_stock_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.available_stock_num:
            if hasattr(self.available_stock_num, 'to_alipay_dict'):
                params['available_stock_num'] = self.available_stock_num.to_alipay_dict()
            else:
                params['available_stock_num'] = self.available_stock_num
        if self.stock_num:
            if hasattr(self.stock_num, 'to_alipay_dict'):
                params['stock_num'] = self.stock_num.to_alipay_dict()
            else:
                params['stock_num'] = self.stock_num
        if self.withholding_stock_num:
            if hasattr(self.withholding_stock_num, 'to_alipay_dict'):
                params['withholding_stock_num'] = self.withholding_stock_num.to_alipay_dict()
            else:
                params['withholding_stock_num'] = self.withholding_stock_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SpuStock()
        if 'available_stock_num' in d:
            o.available_stock_num = d['available_stock_num']
        if 'stock_num' in d:
            o.stock_num = d['stock_num']
        if 'withholding_stock_num' in d:
            o.withholding_stock_num = d['withholding_stock_num']
        return o


