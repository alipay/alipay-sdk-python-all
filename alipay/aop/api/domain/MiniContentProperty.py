#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniContentProperty(object):

    def __init__(self):
        self._key = None
        self._status = None
        self._value_list = None

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
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
        if self.key:
            if hasattr(self.key, 'to_alipay_dict'):
                params['key'] = self.key.to_alipay_dict()
            else:
                params['key'] = self.key
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
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
        o = MiniContentProperty()
        if 'key' in d:
            o.key = d['key']
        if 'status' in d:
            o.status = d['status']
        if 'value_list' in d:
            o.value_list = d['value_list']
        return o


