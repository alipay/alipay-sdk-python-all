#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MaiseDataSATest(object):

    def __init__(self):
        self._key_a = None
        self._key_b = None
        self._key_c = None

    @property
    def key_a(self):
        return self._key_a

    @key_a.setter
    def key_a(self, value):
        self._key_a = value
    @property
    def key_b(self):
        return self._key_b

    @key_b.setter
    def key_b(self, value):
        self._key_b = value
    @property
    def key_c(self):
        return self._key_c

    @key_c.setter
    def key_c(self, value):
        self._key_c = value


    def to_alipay_dict(self):
        params = dict()
        if self.key_a:
            if hasattr(self.key_a, 'to_alipay_dict'):
                params['key_a'] = self.key_a.to_alipay_dict()
            else:
                params['key_a'] = self.key_a
        if self.key_b:
            if hasattr(self.key_b, 'to_alipay_dict'):
                params['key_b'] = self.key_b.to_alipay_dict()
            else:
                params['key_b'] = self.key_b
        if self.key_c:
            if hasattr(self.key_c, 'to_alipay_dict'):
                params['key_c'] = self.key_c.to_alipay_dict()
            else:
                params['key_c'] = self.key_c
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MaiseDataSATest()
        if 'key_a' in d:
            o.key_a = d['key_a']
        if 'key_b' in d:
            o.key_b = d['key_b']
        if 'key_c' in d:
            o.key_c = d['key_c']
        return o


