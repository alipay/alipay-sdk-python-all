#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConditionEntry(object):

    def __init__(self):
        self._dim_key = None
        self._value = None

    @property
    def dim_key(self):
        return self._dim_key

    @dim_key.setter
    def dim_key(self, value):
        self._dim_key = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.dim_key:
            if hasattr(self.dim_key, 'to_alipay_dict'):
                params['dim_key'] = self.dim_key.to_alipay_dict()
            else:
                params['dim_key'] = self.dim_key
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
        o = ConditionEntry()
        if 'dim_key' in d:
            o.dim_key = d['dim_key']
        if 'value' in d:
            o.value = d['value']
        return o


