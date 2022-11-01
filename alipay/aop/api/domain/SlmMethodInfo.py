#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ServeParamInfo import ServeParamInfo


class SlmMethodInfo(object):

    def __init__(self):
        self._method_desc = None
        self._method_name = None
        self._param_info_list = None

    @property
    def method_desc(self):
        return self._method_desc

    @method_desc.setter
    def method_desc(self, value):
        self._method_desc = value
    @property
    def method_name(self):
        return self._method_name

    @method_name.setter
    def method_name(self, value):
        self._method_name = value
    @property
    def param_info_list(self):
        return self._param_info_list

    @param_info_list.setter
    def param_info_list(self, value):
        if isinstance(value, ServeParamInfo):
            self._param_info_list = value
        else:
            self._param_info_list = ServeParamInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.method_desc:
            if hasattr(self.method_desc, 'to_alipay_dict'):
                params['method_desc'] = self.method_desc.to_alipay_dict()
            else:
                params['method_desc'] = self.method_desc
        if self.method_name:
            if hasattr(self.method_name, 'to_alipay_dict'):
                params['method_name'] = self.method_name.to_alipay_dict()
            else:
                params['method_name'] = self.method_name
        if self.param_info_list:
            if hasattr(self.param_info_list, 'to_alipay_dict'):
                params['param_info_list'] = self.param_info_list.to_alipay_dict()
            else:
                params['param_info_list'] = self.param_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SlmMethodInfo()
        if 'method_desc' in d:
            o.method_desc = d['method_desc']
        if 'method_name' in d:
            o.method_name = d['method_name']
        if 'param_info_list' in d:
            o.param_info_list = d['param_info_list']
        return o


