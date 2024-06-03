#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DetailInfo(object):

    def __init__(self):
        self._data_name = None
        self._data_value = None

    @property
    def data_name(self):
        return self._data_name

    @data_name.setter
    def data_name(self, value):
        self._data_name = value
    @property
    def data_value(self):
        return self._data_value

    @data_value.setter
    def data_value(self, value):
        self._data_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_name:
            if hasattr(self.data_name, 'to_alipay_dict'):
                params['data_name'] = self.data_name.to_alipay_dict()
            else:
                params['data_name'] = self.data_name
        if self.data_value:
            if hasattr(self.data_value, 'to_alipay_dict'):
                params['data_value'] = self.data_value.to_alipay_dict()
            else:
                params['data_value'] = self.data_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DetailInfo()
        if 'data_name' in d:
            o.data_name = d['data_name']
        if 'data_value' in d:
            o.data_value = d['data_value']
        return o


