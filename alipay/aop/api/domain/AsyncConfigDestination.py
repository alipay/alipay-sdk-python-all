#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AsyncConfigDestination(object):

    def __init__(self):
        self._destination_type = None
        self._function_name = None

    @property
    def destination_type(self):
        return self._destination_type

    @destination_type.setter
    def destination_type(self, value):
        self._destination_type = value
    @property
    def function_name(self):
        return self._function_name

    @function_name.setter
    def function_name(self, value):
        self._function_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.destination_type:
            if hasattr(self.destination_type, 'to_alipay_dict'):
                params['destination_type'] = self.destination_type.to_alipay_dict()
            else:
                params['destination_type'] = self.destination_type
        if self.function_name:
            if hasattr(self.function_name, 'to_alipay_dict'):
                params['function_name'] = self.function_name.to_alipay_dict()
            else:
                params['function_name'] = self.function_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AsyncConfigDestination()
        if 'destination_type' in d:
            o.destination_type = d['destination_type']
        if 'function_name' in d:
            o.function_name = d['function_name']
        return o


