#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PowerInputPointDTO(object):

    def __init__(self):
        self._data_time = None
        self._value = None

    @property
    def data_time(self):
        return self._data_time

    @data_time.setter
    def data_time(self, value):
        self._data_time = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_time:
            if hasattr(self.data_time, 'to_alipay_dict'):
                params['data_time'] = self.data_time.to_alipay_dict()
            else:
                params['data_time'] = self.data_time
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PowerInputPointDTO()
        if 'data_time' in d:
            o.data_time = d['data_time']
        if 'value' in d:
            o.value = d['value']
        return o


