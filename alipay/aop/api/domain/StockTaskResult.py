#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.StockQuantity import StockQuantity
from alipay.aop.api.domain.StockQueryCondition import StockQueryCondition


class StockTaskResult(object):

    def __init__(self):
        self._charge_type = None
        self._query_time = None
        self._sell_mode = None
        self._stock_quantity = None
        self._stock_query_condition = None
        self._task_id = None
        self._unit_price = None

    @property
    def charge_type(self):
        return self._charge_type

    @charge_type.setter
    def charge_type(self, value):
        self._charge_type = value
    @property
    def query_time(self):
        return self._query_time

    @query_time.setter
    def query_time(self, value):
        self._query_time = value
    @property
    def sell_mode(self):
        return self._sell_mode

    @sell_mode.setter
    def sell_mode(self, value):
        self._sell_mode = value
    @property
    def stock_quantity(self):
        return self._stock_quantity

    @stock_quantity.setter
    def stock_quantity(self, value):
        if isinstance(value, list):
            self._stock_quantity = list()
            for i in value:
                if isinstance(i, StockQuantity):
                    self._stock_quantity.append(i)
                else:
                    self._stock_quantity.append(StockQuantity.from_alipay_dict(i))
    @property
    def stock_query_condition(self):
        return self._stock_query_condition

    @stock_query_condition.setter
    def stock_query_condition(self, value):
        if isinstance(value, StockQueryCondition):
            self._stock_query_condition = value
        else:
            self._stock_query_condition = StockQueryCondition.from_alipay_dict(value)
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        self._unit_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.charge_type:
            if hasattr(self.charge_type, 'to_alipay_dict'):
                params['charge_type'] = self.charge_type.to_alipay_dict()
            else:
                params['charge_type'] = self.charge_type
        if self.query_time:
            if hasattr(self.query_time, 'to_alipay_dict'):
                params['query_time'] = self.query_time.to_alipay_dict()
            else:
                params['query_time'] = self.query_time
        if self.sell_mode:
            if hasattr(self.sell_mode, 'to_alipay_dict'):
                params['sell_mode'] = self.sell_mode.to_alipay_dict()
            else:
                params['sell_mode'] = self.sell_mode
        if self.stock_quantity:
            if isinstance(self.stock_quantity, list):
                for i in range(0, len(self.stock_quantity)):
                    element = self.stock_quantity[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.stock_quantity[i] = element.to_alipay_dict()
            if hasattr(self.stock_quantity, 'to_alipay_dict'):
                params['stock_quantity'] = self.stock_quantity.to_alipay_dict()
            else:
                params['stock_quantity'] = self.stock_quantity
        if self.stock_query_condition:
            if hasattr(self.stock_query_condition, 'to_alipay_dict'):
                params['stock_query_condition'] = self.stock_query_condition.to_alipay_dict()
            else:
                params['stock_query_condition'] = self.stock_query_condition
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.unit_price:
            if hasattr(self.unit_price, 'to_alipay_dict'):
                params['unit_price'] = self.unit_price.to_alipay_dict()
            else:
                params['unit_price'] = self.unit_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StockTaskResult()
        if 'charge_type' in d:
            o.charge_type = d['charge_type']
        if 'query_time' in d:
            o.query_time = d['query_time']
        if 'sell_mode' in d:
            o.sell_mode = d['sell_mode']
        if 'stock_quantity' in d:
            o.stock_quantity = d['stock_quantity']
        if 'stock_query_condition' in d:
            o.stock_query_condition = d['stock_query_condition']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'unit_price' in d:
            o.unit_price = d['unit_price']
        return o


