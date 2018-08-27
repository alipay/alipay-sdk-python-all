#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZmWatchListExtendInfo(object):

    def __init__(self):
        self._description = None
        self._key = None
        self._value = None

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
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
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.key:
            if hasattr(self.key, 'to_alipay_dict'):
                params['key'] = self.key.to_alipay_dict()
            else:
                params['key'] = self.key
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
        o = ZmWatchListExtendInfo()
        if 'description' in d:
            o.description = d['description']
        if 'key' in d:
            o.key = d['key']
        if 'value' in d:
            o.value = d['value']
        return o


