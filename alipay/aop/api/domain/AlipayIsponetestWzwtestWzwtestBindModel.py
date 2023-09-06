#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TestDemoWzw import TestDemoWzw


class AlipayIsponetestWzwtestWzwtestBindModel(object):

    def __init__(self):
        self._complex_1 = None
        self._number_c = None
        self._number_d = None
        self._string = None
        self._string_a = None
        self._string_b = None

    @property
    def complex_1(self):
        return self._complex_1

    @complex_1.setter
    def complex_1(self, value):
        if isinstance(value, TestDemoWzw):
            self._complex_1 = value
        else:
            self._complex_1 = TestDemoWzw.from_alipay_dict(value)
    @property
    def number_c(self):
        return self._number_c

    @number_c.setter
    def number_c(self, value):
        self._number_c = value
    @property
    def number_d(self):
        return self._number_d

    @number_d.setter
    def number_d(self, value):
        self._number_d = value
    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, value):
        self._string = value
    @property
    def string_a(self):
        return self._string_a

    @string_a.setter
    def string_a(self, value):
        self._string_a = value
    @property
    def string_b(self):
        return self._string_b

    @string_b.setter
    def string_b(self, value):
        self._string_b = value


    def to_alipay_dict(self):
        params = dict()
        if self.complex_1:
            if hasattr(self.complex_1, 'to_alipay_dict'):
                params['complex_1'] = self.complex_1.to_alipay_dict()
            else:
                params['complex_1'] = self.complex_1
        if self.number_c:
            if hasattr(self.number_c, 'to_alipay_dict'):
                params['number_c'] = self.number_c.to_alipay_dict()
            else:
                params['number_c'] = self.number_c
        if self.number_d:
            if hasattr(self.number_d, 'to_alipay_dict'):
                params['number_d'] = self.number_d.to_alipay_dict()
            else:
                params['number_d'] = self.number_d
        if self.string:
            if hasattr(self.string, 'to_alipay_dict'):
                params['string'] = self.string.to_alipay_dict()
            else:
                params['string'] = self.string
        if self.string_a:
            if hasattr(self.string_a, 'to_alipay_dict'):
                params['string_a'] = self.string_a.to_alipay_dict()
            else:
                params['string_a'] = self.string_a
        if self.string_b:
            if hasattr(self.string_b, 'to_alipay_dict'):
                params['string_b'] = self.string_b.to_alipay_dict()
            else:
                params['string_b'] = self.string_b
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIsponetestWzwtestWzwtestBindModel()
        if 'complex_1' in d:
            o.complex_1 = d['complex_1']
        if 'number_c' in d:
            o.number_c = d['number_c']
        if 'number_d' in d:
            o.number_d = d['number_d']
        if 'string' in d:
            o.string = d['string']
        if 'string_a' in d:
            o.string_a = d['string_a']
        if 'string_b' in d:
            o.string_b = d['string_b']
        return o


