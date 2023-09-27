#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MonitorFilter(object):

    def __init__(self):
        self._function_name = None
        self._mongodb_operation = None
        self._oss_operation = None

    @property
    def function_name(self):
        return self._function_name

    @function_name.setter
    def function_name(self, value):
        self._function_name = value
    @property
    def mongodb_operation(self):
        return self._mongodb_operation

    @mongodb_operation.setter
    def mongodb_operation(self, value):
        self._mongodb_operation = value
    @property
    def oss_operation(self):
        return self._oss_operation

    @oss_operation.setter
    def oss_operation(self, value):
        self._oss_operation = value


    def to_alipay_dict(self):
        params = dict()
        if self.function_name:
            if hasattr(self.function_name, 'to_alipay_dict'):
                params['function_name'] = self.function_name.to_alipay_dict()
            else:
                params['function_name'] = self.function_name
        if self.mongodb_operation:
            if hasattr(self.mongodb_operation, 'to_alipay_dict'):
                params['mongodb_operation'] = self.mongodb_operation.to_alipay_dict()
            else:
                params['mongodb_operation'] = self.mongodb_operation
        if self.oss_operation:
            if hasattr(self.oss_operation, 'to_alipay_dict'):
                params['oss_operation'] = self.oss_operation.to_alipay_dict()
            else:
                params['oss_operation'] = self.oss_operation
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MonitorFilter()
        if 'function_name' in d:
            o.function_name = d['function_name']
        if 'mongodb_operation' in d:
            o.mongodb_operation = d['mongodb_operation']
        if 'oss_operation' in d:
            o.oss_operation = d['oss_operation']
        return o


