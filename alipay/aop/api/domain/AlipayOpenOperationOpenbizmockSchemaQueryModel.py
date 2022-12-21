#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenOperationOpenbizmockSchemaQueryModel(object):

    def __init__(self):
        self._a = None
        self._b = None
        self._c = None

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value
    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = value
    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, value):
        self._c = value


    def to_alipay_dict(self):
        params = dict()
        if self.a:
            if hasattr(self.a, 'to_alipay_dict'):
                params['a'] = self.a.to_alipay_dict()
            else:
                params['a'] = self.a
        if self.b:
            if hasattr(self.b, 'to_alipay_dict'):
                params['b'] = self.b.to_alipay_dict()
            else:
                params['b'] = self.b
        if self.c:
            if hasattr(self.c, 'to_alipay_dict'):
                params['c'] = self.c.to_alipay_dict()
            else:
                params['c'] = self.c
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOperationOpenbizmockSchemaQueryModel()
        if 'a' in d:
            o.a = d['a']
        if 'b' in d:
            o.b = d['b']
        if 'c' in d:
            o.c = d['c']
        return o


