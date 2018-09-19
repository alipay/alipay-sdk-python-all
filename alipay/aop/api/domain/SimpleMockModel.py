#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SimpleMockModel(object):

    def __init__(self):
        self._count_items = None
        self._happen_time = None
        self._price_num = None
        self._right = None
        self._trade_no = None

    @property
    def count_items(self):
        return self._count_items

    @count_items.setter
    def count_items(self, value):
        self._count_items = value
    @property
    def happen_time(self):
        return self._happen_time

    @happen_time.setter
    def happen_time(self, value):
        self._happen_time = value
    @property
    def price_num(self):
        return self._price_num

    @price_num.setter
    def price_num(self, value):
        self._price_num = value
    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        self._right = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.count_items:
            if hasattr(self.count_items, 'to_alipay_dict'):
                params['count_items'] = self.count_items.to_alipay_dict()
            else:
                params['count_items'] = self.count_items
        if self.happen_time:
            if hasattr(self.happen_time, 'to_alipay_dict'):
                params['happen_time'] = self.happen_time.to_alipay_dict()
            else:
                params['happen_time'] = self.happen_time
        if self.price_num:
            if hasattr(self.price_num, 'to_alipay_dict'):
                params['price_num'] = self.price_num.to_alipay_dict()
            else:
                params['price_num'] = self.price_num
        if self.right:
            if hasattr(self.right, 'to_alipay_dict'):
                params['right'] = self.right.to_alipay_dict()
            else:
                params['right'] = self.right
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SimpleMockModel()
        if 'count_items' in d:
            o.count_items = d['count_items']
        if 'happen_time' in d:
            o.happen_time = d['happen_time']
        if 'price_num' in d:
            o.price_num = d['price_num']
        if 'right' in d:
            o.right = d['right']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


