#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InteligentDataCondition(object):

    def __init__(self):
        self._data_type = None
        self._limit_type = None
        self._value = None

    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def limit_type(self):
        return self._limit_type

    @limit_type.setter
    def limit_type(self, value):
        self._limit_type = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.limit_type:
            if hasattr(self.limit_type, 'to_alipay_dict'):
                params['limit_type'] = self.limit_type.to_alipay_dict()
            else:
                params['limit_type'] = self.limit_type
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InteligentDataCondition()
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'limit_type' in d:
            o.limit_type = d['limit_type']
        if 'value' in d:
            o.value = d['value']
        return o


