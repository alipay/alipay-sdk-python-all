#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Condition(object):

    def __init__(self):
        self._field_name = None
        self._field_value = None
        self._operator = None

    @property
    def field_name(self):
        return self._field_name

    @field_name.setter
    def field_name(self, value):
        self._field_name = value
    @property
    def field_value(self):
        return self._field_value

    @field_value.setter
    def field_value(self, value):
        self._field_value = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value


    def to_alipay_dict(self):
        params = dict()
        if self.field_name:
            if hasattr(self.field_name, 'to_alipay_dict'):
                params['field_name'] = self.field_name.to_alipay_dict()
            else:
                params['field_name'] = self.field_name
        if self.field_value:
            if hasattr(self.field_value, 'to_alipay_dict'):
                params['field_value'] = self.field_value.to_alipay_dict()
            else:
                params['field_value'] = self.field_value
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Condition()
        if 'field_name' in d:
            o.field_name = d['field_name']
        if 'field_value' in d:
            o.field_value = d['field_value']
        if 'operator' in d:
            o.operator = d['operator']
        return o


