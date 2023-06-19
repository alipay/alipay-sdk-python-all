#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class JsonParamDemo(object):

    def __init__(self):
        self._array_param = None
        self._bool_param = None
        self._date_param = None
        self._datetime = None
        self._num_param = None
        self._price = None

    @property
    def array_param(self):
        return self._array_param

    @array_param.setter
    def array_param(self, value):
        if isinstance(value, list):
            self._array_param = list()
            for i in value:
                self._array_param.append(i)
    @property
    def bool_param(self):
        return self._bool_param

    @bool_param.setter
    def bool_param(self, value):
        self._bool_param = value
    @property
    def date_param(self):
        return self._date_param

    @date_param.setter
    def date_param(self, value):
        self._date_param = value
    @property
    def datetime(self):
        return self._datetime

    @datetime.setter
    def datetime(self, value):
        self._datetime = value
    @property
    def num_param(self):
        return self._num_param

    @num_param.setter
    def num_param(self, value):
        self._num_param = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value


    def to_alipay_dict(self):
        params = dict()
        if self.array_param:
            if isinstance(self.array_param, list):
                for i in range(0, len(self.array_param)):
                    element = self.array_param[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.array_param[i] = element.to_alipay_dict()
            if hasattr(self.array_param, 'to_alipay_dict'):
                params['array_param'] = self.array_param.to_alipay_dict()
            else:
                params['array_param'] = self.array_param
        if self.bool_param:
            if hasattr(self.bool_param, 'to_alipay_dict'):
                params['bool_param'] = self.bool_param.to_alipay_dict()
            else:
                params['bool_param'] = self.bool_param
        if self.date_param:
            if hasattr(self.date_param, 'to_alipay_dict'):
                params['date_param'] = self.date_param.to_alipay_dict()
            else:
                params['date_param'] = self.date_param
        if self.datetime:
            if hasattr(self.datetime, 'to_alipay_dict'):
                params['datetime'] = self.datetime.to_alipay_dict()
            else:
                params['datetime'] = self.datetime
        if self.num_param:
            if hasattr(self.num_param, 'to_alipay_dict'):
                params['num_param'] = self.num_param.to_alipay_dict()
            else:
                params['num_param'] = self.num_param
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = JsonParamDemo()
        if 'array_param' in d:
            o.array_param = d['array_param']
        if 'bool_param' in d:
            o.bool_param = d['bool_param']
        if 'date_param' in d:
            o.date_param = d['date_param']
        if 'datetime' in d:
            o.datetime = d['datetime']
        if 'num_param' in d:
            o.num_param = d['num_param']
        if 'price' in d:
            o.price = d['price']
        return o


