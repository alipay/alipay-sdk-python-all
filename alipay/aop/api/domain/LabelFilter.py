#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LabelFilter(object):

    def __init__(self):
        self._column_name = None
        self._op = None
        self._values = None

    @property
    def column_name(self):
        return self._column_name

    @column_name.setter
    def column_name(self, value):
        self._column_name = value
    @property
    def op(self):
        return self._op

    @op.setter
    def op(self, value):
        self._op = value
    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, value):
        if isinstance(value, list):
            self._values = list()
            for i in value:
                self._values.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.column_name:
            if hasattr(self.column_name, 'to_alipay_dict'):
                params['column_name'] = self.column_name.to_alipay_dict()
            else:
                params['column_name'] = self.column_name
        if self.op:
            if hasattr(self.op, 'to_alipay_dict'):
                params['op'] = self.op.to_alipay_dict()
            else:
                params['op'] = self.op
        if self.values:
            if isinstance(self.values, list):
                for i in range(0, len(self.values)):
                    element = self.values[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.values[i] = element.to_alipay_dict()
            if hasattr(self.values, 'to_alipay_dict'):
                params['values'] = self.values.to_alipay_dict()
            else:
                params['values'] = self.values
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LabelFilter()
        if 'column_name' in d:
            o.column_name = d['column_name']
        if 'op' in d:
            o.op = d['op']
        if 'values' in d:
            o.values = d['values']
        return o


