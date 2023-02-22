#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenidComplex import OpenidComplex


class AlipayOpenAppTestTestChargeModel(object):

    def __init__(self):
        self._a = None
        self._b = None
        self._c = None
        self._complex_param = None
        self._d = None

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
    def complex_param(self):
        return self._complex_param

    @complex_param.setter
    def complex_param(self, value):
        if isinstance(value, OpenidComplex):
            self._complex_param = value
        else:
            self._complex_param = OpenidComplex.from_alipay_dict(value)
    @property
    def d(self):
        return self._d

    @d.setter
    def d(self, value):
        self._d = value


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
        if self.complex_param:
            if hasattr(self.complex_param, 'to_alipay_dict'):
                params['complex_param'] = self.complex_param.to_alipay_dict()
            else:
                params['complex_param'] = self.complex_param
        if self.d:
            if hasattr(self.d, 'to_alipay_dict'):
                params['d'] = self.d.to_alipay_dict()
            else:
                params['d'] = self.d
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppTestTestChargeModel()
        if 'a' in d:
            o.a = d['a']
        if 'b' in d:
            o.b = d['b']
        if 'c' in d:
            o.c = d['c']
        if 'complex_param' in d:
            o.complex_param = d['complex_param']
        if 'd' in d:
            o.d = d['d']
        return o


