#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenOperationOpenbizmockTesttestnumberQueryModel(object):

    def __init__(self):
        self._a = None
        self._b = None
        self._c = None
        self._keykey = None
        self._test_1 = None
        self._test_2 = None

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
    def keykey(self):
        return self._keykey

    @keykey.setter
    def keykey(self, value):
        self._keykey = value
    @property
    def test_1(self):
        return self._test_1

    @test_1.setter
    def test_1(self, value):
        self._test_1 = value
    @property
    def test_2(self):
        return self._test_2

    @test_2.setter
    def test_2(self, value):
        self._test_2 = value


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
        if self.keykey:
            if hasattr(self.keykey, 'to_alipay_dict'):
                params['keykey'] = self.keykey.to_alipay_dict()
            else:
                params['keykey'] = self.keykey
        if self.test_1:
            if hasattr(self.test_1, 'to_alipay_dict'):
                params['test_1'] = self.test_1.to_alipay_dict()
            else:
                params['test_1'] = self.test_1
        if self.test_2:
            if hasattr(self.test_2, 'to_alipay_dict'):
                params['test_2'] = self.test_2.to_alipay_dict()
            else:
                params['test_2'] = self.test_2
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOperationOpenbizmockTesttestnumberQueryModel()
        if 'a' in d:
            o.a = d['a']
        if 'b' in d:
            o.b = d['b']
        if 'c' in d:
            o.c = d['c']
        if 'keykey' in d:
            o.keykey = d['keykey']
        if 'test_1' in d:
            o.test_1 = d['test_1']
        if 'test_2' in d:
            o.test_2 = d['test_2']
        return o


