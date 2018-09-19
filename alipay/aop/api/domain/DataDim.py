#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DataDim(object):

    def __init__(self):
        self._dim_name = None
        self._dim_type = None
        self._dim_value = None

    @property
    def dim_name(self):
        return self._dim_name

    @dim_name.setter
    def dim_name(self, value):
        self._dim_name = value
    @property
    def dim_type(self):
        return self._dim_type

    @dim_type.setter
    def dim_type(self, value):
        self._dim_type = value
    @property
    def dim_value(self):
        return self._dim_value

    @dim_value.setter
    def dim_value(self, value):
        self._dim_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.dim_name:
            if hasattr(self.dim_name, 'to_alipay_dict'):
                params['dim_name'] = self.dim_name.to_alipay_dict()
            else:
                params['dim_name'] = self.dim_name
        if self.dim_type:
            if hasattr(self.dim_type, 'to_alipay_dict'):
                params['dim_type'] = self.dim_type.to_alipay_dict()
            else:
                params['dim_type'] = self.dim_type
        if self.dim_value:
            if hasattr(self.dim_value, 'to_alipay_dict'):
                params['dim_value'] = self.dim_value.to_alipay_dict()
            else:
                params['dim_value'] = self.dim_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DataDim()
        if 'dim_name' in d:
            o.dim_name = d['dim_name']
        if 'dim_type' in d:
            o.dim_type = d['dim_type']
        if 'dim_value' in d:
            o.dim_value = d['dim_value']
        return o


