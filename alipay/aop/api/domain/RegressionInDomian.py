#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RegressionInDomian(object):

    def __init__(self):
        self._a_test_a = None
        self._bb = None
        self._cc = None
        self._input_b = None

    @property
    def a_test_a(self):
        return self._a_test_a

    @a_test_a.setter
    def a_test_a(self, value):
        self._a_test_a = value
    @property
    def bb(self):
        return self._bb

    @bb.setter
    def bb(self, value):
        self._bb = value
    @property
    def cc(self):
        return self._cc

    @cc.setter
    def cc(self, value):
        self._cc = value
    @property
    def input_b(self):
        return self._input_b

    @input_b.setter
    def input_b(self, value):
        self._input_b = value


    def to_alipay_dict(self):
        params = dict()
        if self.a_test_a:
            if hasattr(self.a_test_a, 'to_alipay_dict'):
                params['a_test_a'] = self.a_test_a.to_alipay_dict()
            else:
                params['a_test_a'] = self.a_test_a
        if self.bb:
            if hasattr(self.bb, 'to_alipay_dict'):
                params['bb'] = self.bb.to_alipay_dict()
            else:
                params['bb'] = self.bb
        if self.cc:
            if hasattr(self.cc, 'to_alipay_dict'):
                params['cc'] = self.cc.to_alipay_dict()
            else:
                params['cc'] = self.cc
        if self.input_b:
            if hasattr(self.input_b, 'to_alipay_dict'):
                params['input_b'] = self.input_b.to_alipay_dict()
            else:
                params['input_b'] = self.input_b
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RegressionInDomian()
        if 'a_test_a' in d:
            o.a_test_a = d['a_test_a']
        if 'bb' in d:
            o.bb = d['bb']
        if 'cc' in d:
            o.cc = d['cc']
        if 'input_b' in d:
            o.input_b = d['input_b']
        return o


