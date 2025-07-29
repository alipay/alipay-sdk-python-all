#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FileValueRequest import FileValueRequest


class CurrentChatFiles(object):

    def __init__(self):
        self._type = None
        self._value = None

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, list):
            self._value = list()
            for i in value:
                if isinstance(i, FileValueRequest):
                    self._value.append(i)
                else:
                    self._value.append(FileValueRequest.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
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
        o = CurrentChatFiles()
        if 'type' in d:
            o.type = d['type']
        if 'value' in d:
            o.value = d['value']
        return o


