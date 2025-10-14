#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemStockUpdateByIsvItemIdParam(object):

    def __init__(self):
        self._end_time = None
        self._isv_item_id = None
        self._start_time = None
        self._stock = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def isv_item_id(self):
        return self._isv_item_id

    @isv_item_id.setter
    def isv_item_id(self, value):
        self._isv_item_id = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        self._stock = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.isv_item_id:
            if hasattr(self.isv_item_id, 'to_alipay_dict'):
                params['isv_item_id'] = self.isv_item_id.to_alipay_dict()
            else:
                params['isv_item_id'] = self.isv_item_id
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
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
        o = ItemStockUpdateByIsvItemIdParam()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'isv_item_id' in d:
            o.isv_item_id = d['isv_item_id']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'stock' in d:
            o.stock = d['stock']
        return o


