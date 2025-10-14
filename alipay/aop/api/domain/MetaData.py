#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MetaData(object):

    def __init__(self):
        self._meta_data_code = None
        self._meta_data_desc = None
        self._meta_data_name = None
        self._simple_value = None

    @property
    def meta_data_code(self):
        return self._meta_data_code

    @meta_data_code.setter
    def meta_data_code(self, value):
        self._meta_data_code = value
    @property
    def meta_data_desc(self):
        return self._meta_data_desc

    @meta_data_desc.setter
    def meta_data_desc(self, value):
        self._meta_data_desc = value
    @property
    def meta_data_name(self):
        return self._meta_data_name

    @meta_data_name.setter
    def meta_data_name(self, value):
        self._meta_data_name = value
    @property
    def simple_value(self):
        return self._simple_value

    @simple_value.setter
    def simple_value(self, value):
        self._simple_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.meta_data_code:
            if hasattr(self.meta_data_code, 'to_alipay_dict'):
                params['meta_data_code'] = self.meta_data_code.to_alipay_dict()
            else:
                params['meta_data_code'] = self.meta_data_code
        if self.meta_data_desc:
            if hasattr(self.meta_data_desc, 'to_alipay_dict'):
                params['meta_data_desc'] = self.meta_data_desc.to_alipay_dict()
            else:
                params['meta_data_desc'] = self.meta_data_desc
        if self.meta_data_name:
            if hasattr(self.meta_data_name, 'to_alipay_dict'):
                params['meta_data_name'] = self.meta_data_name.to_alipay_dict()
            else:
                params['meta_data_name'] = self.meta_data_name
        if self.simple_value:
            if hasattr(self.simple_value, 'to_alipay_dict'):
                params['simple_value'] = self.simple_value.to_alipay_dict()
            else:
                params['simple_value'] = self.simple_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MetaData()
        if 'meta_data_code' in d:
            o.meta_data_code = d['meta_data_code']
        if 'meta_data_desc' in d:
            o.meta_data_desc = d['meta_data_desc']
        if 'meta_data_name' in d:
            o.meta_data_name = d['meta_data_name']
        if 'simple_value' in d:
            o.simple_value = d['simple_value']
        return o


