#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FillContent(object):

    def __init__(self):
        self._struct_key = None
        self._value = None

    @property
    def struct_key(self):
        return self._struct_key

    @struct_key.setter
    def struct_key(self, value):
        self._struct_key = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.struct_key:
            if hasattr(self.struct_key, 'to_alipay_dict'):
                params['struct_key'] = self.struct_key.to_alipay_dict()
            else:
                params['struct_key'] = self.struct_key
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
        o = FillContent()
        if 'struct_key' in d:
            o.struct_key = d['struct_key']
        if 'value' in d:
            o.value = d['value']
        return o


