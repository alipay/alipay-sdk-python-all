#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceAttributeSimpleVO(object):

    def __init__(self):
        self._key = None
        self._value = None

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, list):
            self._value = list()
            for i in value:
                self._value.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.key:
            if hasattr(self.key, 'to_alipay_dict'):
                params['key'] = self.key.to_alipay_dict()
            else:
                params['key'] = self.key
        if self.value:
            if isinstance(self.value, list):
                for i in range(0, len(self.value)):
                    element = self.value[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.value[i] = element.to_alipay_dict()
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceAttributeSimpleVO()
        if 'key' in d:
            o.key = d['key']
        if 'value' in d:
            o.value = d['value']
        return o


