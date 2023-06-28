#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AAAAAtest import AAAAAtest


class AlipayOpenOperationOpenbizmockTestdcQueryModel(object):

    def __init__(self):
        self._a = None
        self._b = None
        self._c = None
        self._d = None
        self._e = None
        self._g = None
        self._i = None

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
    @property
    def d(self):
        return self._d

    @d.setter
    def d(self, value):
        self._d = value
    @property
    def e(self):
        return self._e

    @e.setter
    def e(self, value):
        self._e = value
    @property
    def g(self):
        return self._g

    @g.setter
    def g(self, value):
        if isinstance(value, AAAAAtest):
            self._g = value
        else:
            self._g = AAAAAtest.from_alipay_dict(value)
    @property
    def i(self):
        return self._i

    @i.setter
    def i(self, value):
        if isinstance(value, list):
            self._i = list()
            for i in value:
                self._i.append(i)


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
        if self.d:
            if hasattr(self.d, 'to_alipay_dict'):
                params['d'] = self.d.to_alipay_dict()
            else:
                params['d'] = self.d
        if self.e:
            if hasattr(self.e, 'to_alipay_dict'):
                params['e'] = self.e.to_alipay_dict()
            else:
                params['e'] = self.e
        if self.g:
            if hasattr(self.g, 'to_alipay_dict'):
                params['g'] = self.g.to_alipay_dict()
            else:
                params['g'] = self.g
        if self.i:
            if isinstance(self.i, list):
                for i in range(0, len(self.i)):
                    element = self.i[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.i[i] = element.to_alipay_dict()
            if hasattr(self.i, 'to_alipay_dict'):
                params['i'] = self.i.to_alipay_dict()
            else:
                params['i'] = self.i
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOperationOpenbizmockTestdcQueryModel()
        if 'a' in d:
            o.a = d['a']
        if 'b' in d:
            o.b = d['b']
        if 'c' in d:
            o.c = d['c']
        if 'd' in d:
            o.d = d['d']
        if 'e' in d:
            o.e = d['e']
        if 'g' in d:
            o.g = d['g']
        if 'i' in d:
            o.i = d['i']
        return o


