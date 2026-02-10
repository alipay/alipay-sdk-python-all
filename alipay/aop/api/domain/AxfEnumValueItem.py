#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AxfEnumValueItem(object):

    def __init__(self):
        self._enum_key = None
        self._enum_value = None

    @property
    def enum_key(self):
        return self._enum_key

    @enum_key.setter
    def enum_key(self, value):
        self._enum_key = value
    @property
    def enum_value(self):
        return self._enum_value

    @enum_value.setter
    def enum_value(self, value):
        self._enum_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.enum_key:
            if hasattr(self.enum_key, 'to_alipay_dict'):
                params['enum_key'] = self.enum_key.to_alipay_dict()
            else:
                params['enum_key'] = self.enum_key
        if self.enum_value:
            if hasattr(self.enum_value, 'to_alipay_dict'):
                params['enum_value'] = self.enum_value.to_alipay_dict()
            else:
                params['enum_value'] = self.enum_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AxfEnumValueItem()
        if 'enum_key' in d:
            o.enum_key = d['enum_key']
        if 'enum_value' in d:
            o.enum_value = d['enum_value']
        return o


