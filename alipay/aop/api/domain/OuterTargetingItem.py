#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OuterTargetingItem(object):

    def __init__(self):
        self._type = None
        self._value_list = None

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def value_list(self):
        return self._value_list

    @value_list.setter
    def value_list(self, value):
        if isinstance(value, list):
            self._value_list = list()
            for i in value:
                self._value_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.value_list:
            if isinstance(self.value_list, list):
                for i in range(0, len(self.value_list)):
                    element = self.value_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.value_list[i] = element.to_alipay_dict()
            if hasattr(self.value_list, 'to_alipay_dict'):
                params['value_list'] = self.value_list.to_alipay_dict()
            else:
                params['value_list'] = self.value_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OuterTargetingItem()
        if 'type' in d:
            o.type = d['type']
        if 'value_list' in d:
            o.value_list = d['value_list']
        return o


