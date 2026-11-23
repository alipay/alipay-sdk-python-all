#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConfigParam(object):

    def __init__(self):
        self._param_name = None
        self._param_type = None
        self._param_value = None
        self._param_value_type = None

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
    def param_value(self):
        return self._param_value

    @param_value.setter
    def param_value(self, value):
        self._param_value = value
    @property
    def param_value_type(self):
        return self._param_value_type

    @param_value_type.setter
    def param_value_type(self, value):
        self._param_value_type = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.param_value:
            if hasattr(self.param_value, 'to_alipay_dict'):
                params['param_value'] = self.param_value.to_alipay_dict()
            else:
                params['param_value'] = self.param_value
        if self.param_value_type:
            if hasattr(self.param_value_type, 'to_alipay_dict'):
                params['param_value_type'] = self.param_value_type.to_alipay_dict()
            else:
                params['param_value_type'] = self.param_value_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConfigParam()
        if 'param_name' in d:
            o.param_name = d['param_name']
        if 'param_type' in d:
            o.param_type = d['param_type']
        if 'param_value' in d:
            o.param_value = d['param_value']
        if 'param_value_type' in d:
            o.param_value_type = d['param_value_type']
        return o


