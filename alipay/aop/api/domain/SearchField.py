#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SearchField(object):

    def __init__(self):
        self._field_code = None
        self._field_operator_type = None
        self._value = None
        self._variable_name = None

    @property
    def field_code(self):
        return self._field_code

    @field_code.setter
    def field_code(self, value):
        self._field_code = value
    @property
    def field_operator_type(self):
        return self._field_operator_type

    @field_operator_type.setter
    def field_operator_type(self, value):
        self._field_operator_type = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
    @property
    def variable_name(self):
        return self._variable_name

    @variable_name.setter
    def variable_name(self, value):
        self._variable_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.field_code:
            if hasattr(self.field_code, 'to_alipay_dict'):
                params['field_code'] = self.field_code.to_alipay_dict()
            else:
                params['field_code'] = self.field_code
        if self.field_operator_type:
            if hasattr(self.field_operator_type, 'to_alipay_dict'):
                params['field_operator_type'] = self.field_operator_type.to_alipay_dict()
            else:
                params['field_operator_type'] = self.field_operator_type
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        if self.variable_name:
            if hasattr(self.variable_name, 'to_alipay_dict'):
                params['variable_name'] = self.variable_name.to_alipay_dict()
            else:
                params['variable_name'] = self.variable_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SearchField()
        if 'field_code' in d:
            o.field_code = d['field_code']
        if 'field_operator_type' in d:
            o.field_operator_type = d['field_operator_type']
        if 'value' in d:
            o.value = d['value']
        if 'variable_name' in d:
            o.variable_name = d['variable_name']
        return o


