#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenModuleData import OpenModuleData


class OpenPayResultModule(object):

    def __init__(self):
        self._open_module_data = None
        self._type = None

    @property
    def open_module_data(self):
        return self._open_module_data

    @open_module_data.setter
    def open_module_data(self, value):
        if isinstance(value, OpenModuleData):
            self._open_module_data = value
        else:
            self._open_module_data = OpenModuleData.from_alipay_dict(value)
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_module_data:
            if hasattr(self.open_module_data, 'to_alipay_dict'):
                params['open_module_data'] = self.open_module_data.to_alipay_dict()
            else:
                params['open_module_data'] = self.open_module_data
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
        o = OpenPayResultModule()
        if 'open_module_data' in d:
            o.open_module_data = d['open_module_data']
        if 'type' in d:
            o.type = d['type']
        return o


