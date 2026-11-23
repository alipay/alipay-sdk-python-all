#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GlobalParam(object):

    def __init__(self):
        self._description = None
        self._example = None
        self._max_length = None
        self._param_name = None
        self._param_type = None
        self._param_value_type = None
        self._required = None

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def example(self):
        return self._example

    @example.setter
    def example(self, value):
        self._example = value
    @property
    def max_length(self):
        return self._max_length

    @max_length.setter
    def max_length(self, value):
        self._max_length = value
    @property
    def param_name(self):
        return self._param_name

    @param_name.setter
    def param_name(self, value):
        self._param_name = value
    @property
    def param_type(self):
        return self._param_type

    @param_type.setter
    def param_type(self, value):
        self._param_type = value
    @property
    def param_value_type(self):
        return self._param_value_type

    @param_value_type.setter
    def param_value_type(self, value):
        self._param_value_type = value
    @property
    def required(self):
        return self._required

    @required.setter
    def required(self, value):
        self._required = value


    def to_alipay_dict(self):
        params = dict()
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.example:
            if hasattr(self.example, 'to_alipay_dict'):
                params['example'] = self.example.to_alipay_dict()
            else:
                params['example'] = self.example
        if self.max_length:
            if hasattr(self.max_length, 'to_alipay_dict'):
                params['max_length'] = self.max_length.to_alipay_dict()
            else:
                params['max_length'] = self.max_length
        if self.param_name:
            if hasattr(self.param_name, 'to_alipay_dict'):
                params['param_name'] = self.param_name.to_alipay_dict()
            else:
                params['param_name'] = self.param_name
        if self.param_type:
            if hasattr(self.param_type, 'to_alipay_dict'):
                params['param_type'] = self.param_type.to_alipay_dict()
            else:
                params['param_type'] = self.param_type
        if self.param_value_type:
            if hasattr(self.param_value_type, 'to_alipay_dict'):
                params['param_value_type'] = self.param_value_type.to_alipay_dict()
            else:
                params['param_value_type'] = self.param_value_type
        if self.required:
            if hasattr(self.required, 'to_alipay_dict'):
                params['required'] = self.required.to_alipay_dict()
            else:
                params['required'] = self.required
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GlobalParam()
        if 'description' in d:
            o.description = d['description']
        if 'example' in d:
            o.example = d['example']
        if 'max_length' in d:
            o.max_length = d['max_length']
        if 'param_name' in d:
            o.param_name = d['param_name']
        if 'param_type' in d:
            o.param_type = d['param_type']
        if 'param_value_type' in d:
            o.param_value_type = d['param_value_type']
        if 'required' in d:
            o.required = d['required']
        return o


