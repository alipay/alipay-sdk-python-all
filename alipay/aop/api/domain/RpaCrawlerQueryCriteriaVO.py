#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RpaCrawlerQueryCriteriaVO(object):

    def __init__(self):
        self._comparison = None
        self._key = None
        self._value = None
        self._value_end = None
        self._value_start = None
        self._values = None

    @property
    def comparison(self):
        return self._comparison

    @comparison.setter
    def comparison(self, value):
        self._comparison = value
    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
    @property
    def value_end(self):
        return self._value_end

    @value_end.setter
    def value_end(self, value):
        self._value_end = value
    @property
    def value_start(self):
        return self._value_start

    @value_start.setter
    def value_start(self, value):
        self._value_start = value
    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, value):
        self._values = value


    def to_alipay_dict(self):
        params = dict()
        if self.comparison:
            if hasattr(self.comparison, 'to_alipay_dict'):
                params['comparison'] = self.comparison.to_alipay_dict()
            else:
                params['comparison'] = self.comparison
        if self.key:
            if hasattr(self.key, 'to_alipay_dict'):
                params['key'] = self.key.to_alipay_dict()
            else:
                params['key'] = self.key
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        if self.value_end:
            if hasattr(self.value_end, 'to_alipay_dict'):
                params['value_end'] = self.value_end.to_alipay_dict()
            else:
                params['value_end'] = self.value_end
        if self.value_start:
            if hasattr(self.value_start, 'to_alipay_dict'):
                params['value_start'] = self.value_start.to_alipay_dict()
            else:
                params['value_start'] = self.value_start
        if self.values:
            if hasattr(self.values, 'to_alipay_dict'):
                params['values'] = self.values.to_alipay_dict()
            else:
                params['values'] = self.values
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RpaCrawlerQueryCriteriaVO()
        if 'comparison' in d:
            o.comparison = d['comparison']
        if 'key' in d:
            o.key = d['key']
        if 'value' in d:
            o.value = d['value']
        if 'value_end' in d:
            o.value_end = d['value_end']
        if 'value_start' in d:
            o.value_start = d['value_start']
        if 'values' in d:
            o.values = d['values']
        return o


