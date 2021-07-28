#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbdishCookDetailSimplifyInfo(object):

    def __init__(self):
        self._out_dish_id = None
        self._out_sku_id = None
        self._sell_price = None
        self._sort = None
        self._time_ranges = None

    @property
    def out_dish_id(self):
        return self._out_dish_id

    @out_dish_id.setter
    def out_dish_id(self, value):
        self._out_dish_id = value
    @property
    def out_sku_id(self):
        return self._out_sku_id

    @out_sku_id.setter
    def out_sku_id(self, value):
        self._out_sku_id = value
    @property
    def sell_price(self):
        return self._sell_price

    @sell_price.setter
    def sell_price(self, value):
        self._sell_price = value
    @property
    def sort(self):
        return self._sort

    @sort.setter
    def sort(self, value):
        self._sort = value
    @property
    def time_ranges(self):
        return self._time_ranges

    @time_ranges.setter
    def time_ranges(self, value):
        if isinstance(value, list):
            self._time_ranges = list()
            for i in value:
                self._time_ranges.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.out_dish_id:
            if hasattr(self.out_dish_id, 'to_alipay_dict'):
                params['out_dish_id'] = self.out_dish_id.to_alipay_dict()
            else:
                params['out_dish_id'] = self.out_dish_id
        if self.out_sku_id:
            if hasattr(self.out_sku_id, 'to_alipay_dict'):
                params['out_sku_id'] = self.out_sku_id.to_alipay_dict()
            else:
                params['out_sku_id'] = self.out_sku_id
        if self.sell_price:
            if hasattr(self.sell_price, 'to_alipay_dict'):
                params['sell_price'] = self.sell_price.to_alipay_dict()
            else:
                params['sell_price'] = self.sell_price
        if self.sort:
            if hasattr(self.sort, 'to_alipay_dict'):
                params['sort'] = self.sort.to_alipay_dict()
            else:
                params['sort'] = self.sort
        if self.time_ranges:
            if isinstance(self.time_ranges, list):
                for i in range(0, len(self.time_ranges)):
                    element = self.time_ranges[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.time_ranges[i] = element.to_alipay_dict()
            if hasattr(self.time_ranges, 'to_alipay_dict'):
                params['time_ranges'] = self.time_ranges.to_alipay_dict()
            else:
                params['time_ranges'] = self.time_ranges
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishCookDetailSimplifyInfo()
        if 'out_dish_id' in d:
            o.out_dish_id = d['out_dish_id']
        if 'out_sku_id' in d:
            o.out_sku_id = d['out_sku_id']
        if 'sell_price' in d:
            o.sell_price = d['sell_price']
        if 'sort' in d:
            o.sort = d['sort']
        if 'time_ranges' in d:
            o.time_ranges = d['time_ranges']
        return o


