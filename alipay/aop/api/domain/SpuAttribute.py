#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SpuAttribute(object):

    def __init__(self):
        self._name = None
        self._value = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
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
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
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
        o = SpuAttribute()
        if 'name' in d:
            o.name = d['name']
        if 'value' in d:
            o.value = d['value']
        return o


