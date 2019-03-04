#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShopExtInfo(object):

    def __init__(self):
        self._key_name = None
        self._value = None

    @property
    def key_name(self):
        return self._key_name

    @key_name.setter
    def key_name(self, value):
        self._key_name = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.key_name:
            if hasattr(self.key_name, 'to_alipay_dict'):
                params['key_name'] = self.key_name.to_alipay_dict()
            else:
                params['key_name'] = self.key_name
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
        o = ShopExtInfo()
        if 'key_name' in d:
            o.key_name = d['key_name']
        if 'value' in d:
            o.value = d['value']
        return o


