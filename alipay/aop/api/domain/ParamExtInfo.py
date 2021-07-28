#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ParamExtInfo(object):

    def __init__(self):
        self._param_name = None
        self._param_value = None
        self._type = None

    @property
    def param_name(self):
        return self._param_name

    @param_name.setter
    def param_name(self, value):
        self._param_name = value
    @property
    def param_value(self):
        return self._param_value

    @param_value.setter
    def param_value(self, value):
        self._param_value = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.param_name:
            if hasattr(self.param_name, 'to_alipay_dict'):
                params['param_name'] = self.param_name.to_alipay_dict()
            else:
                params['param_name'] = self.param_name
        if self.param_value:
            if hasattr(self.param_value, 'to_alipay_dict'):
                params['param_value'] = self.param_value.to_alipay_dict()
            else:
                params['param_value'] = self.param_value
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ParamExtInfo()
        if 'param_name' in d:
            o.param_name = d['param_name']
        if 'param_value' in d:
            o.param_value = d['param_value']
        if 'type' in d:
            o.type = d['type']
        return o


