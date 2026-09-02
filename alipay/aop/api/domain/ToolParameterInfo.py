#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ToolParameterInfo(object):

    def __init__(self):
        self._array = None
        self._default_value = None
        self._param_desc = None
        self._param_name = None
        self._param_type = None
        self._required = None
        self._sub_params = None

    @property
    def array(self):
        return self._array

    @array.setter
    def array(self, value):
        self._array = value
    @property
    def default_value(self):
        return self._default_value

    @default_value.setter
    def default_value(self, value):
        self._default_value = value
    @property
    def param_desc(self):
        return self._param_desc

    @param_desc.setter
    def param_desc(self, value):
        self._param_desc = value
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
    def required(self):
        return self._required

    @required.setter
    def required(self, value):
        self._required = value
    @property
    def sub_params(self):
        return self._sub_params

    @sub_params.setter
    def sub_params(self, value):
        self._sub_params = value


    def to_alipay_dict(self):
        params = dict()
        if self.array:
            if hasattr(self.array, 'to_alipay_dict'):
                params['array'] = self.array.to_alipay_dict()
            else:
                params['array'] = self.array
        if self.default_value:
            if hasattr(self.default_value, 'to_alipay_dict'):
                params['default_value'] = self.default_value.to_alipay_dict()
            else:
                params['default_value'] = self.default_value
        if self.param_desc:
            if hasattr(self.param_desc, 'to_alipay_dict'):
                params['param_desc'] = self.param_desc.to_alipay_dict()
            else:
                params['param_desc'] = self.param_desc
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
        if self.required:
            if hasattr(self.required, 'to_alipay_dict'):
                params['required'] = self.required.to_alipay_dict()
            else:
                params['required'] = self.required
        if self.sub_params:
            if hasattr(self.sub_params, 'to_alipay_dict'):
                params['sub_params'] = self.sub_params.to_alipay_dict()
            else:
                params['sub_params'] = self.sub_params
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ToolParameterInfo()
        if 'array' in d:
            o.array = d['array']
        if 'default_value' in d:
            o.default_value = d['default_value']
        if 'param_desc' in d:
            o.param_desc = d['param_desc']
        if 'param_name' in d:
            o.param_name = d['param_name']
        if 'param_type' in d:
            o.param_type = d['param_type']
        if 'required' in d:
            o.required = d['required']
        if 'sub_params' in d:
            o.sub_params = d['sub_params']
        return o


