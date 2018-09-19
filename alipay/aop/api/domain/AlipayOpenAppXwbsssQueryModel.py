#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppXwbsssQueryModel(object):

    def __init__(self):
        self._a = None
        self._b = None
        self._c = None
        self._effect_date = None

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
        if isinstance(value, list):
            self._c = list()
            for i in value:
                self._c.append(i)
    @property
    def effect_date(self):
        return self._effect_date

    @effect_date.setter
    def effect_date(self, value):
        self._effect_date = value


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
            if isinstance(self.c, list):
                for i in range(0, len(self.c)):
                    element = self.c[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.c[i] = element.to_alipay_dict()
            if hasattr(self.c, 'to_alipay_dict'):
                params['c'] = self.c.to_alipay_dict()
            else:
                params['c'] = self.c
        if self.effect_date:
            if hasattr(self.effect_date, 'to_alipay_dict'):
                params['effect_date'] = self.effect_date.to_alipay_dict()
            else:
                params['effect_date'] = self.effect_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppXwbsssQueryModel()
        if 'a' in d:
            o.a = d['a']
        if 'b' in d:
            o.b = d['b']
        if 'c' in d:
            o.c = d['c']
        if 'effect_date' in d:
            o.effect_date = d['effect_date']
        return o


