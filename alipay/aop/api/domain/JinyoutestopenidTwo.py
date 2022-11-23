#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.JinyoutestopenidOne import JinyoutestopenidOne


class JinyoutestopenidTwo(object):

    def __init__(self):
        self._a = None
        self._b = None
        self._b_open_id = None
        self._f = None

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
    def b_open_id(self):
        return self._b_open_id

    @b_open_id.setter
    def b_open_id(self, value):
        self._b_open_id = value
    @property
    def f(self):
        return self._f

    @f.setter
    def f(self, value):
        if isinstance(value, JinyoutestopenidOne):
            self._f = value
        else:
            self._f = JinyoutestopenidOne.from_alipay_dict(value)


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
        if self.b_open_id:
            if hasattr(self.b_open_id, 'to_alipay_dict'):
                params['b_open_id'] = self.b_open_id.to_alipay_dict()
            else:
                params['b_open_id'] = self.b_open_id
        if self.f:
            if hasattr(self.f, 'to_alipay_dict'):
                params['f'] = self.f.to_alipay_dict()
            else:
                params['f'] = self.f
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = JinyoutestopenidTwo()
        if 'a' in d:
            o.a = d['a']
        if 'b' in d:
            o.b = d['b']
        if 'b_open_id' in d:
            o.b_open_id = d['b_open_id']
        if 'f' in d:
            o.f = d['f']
        return o


