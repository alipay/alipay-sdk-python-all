#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossProdDateTestSendModel(object):

    def __init__(self):
        self._a_open_id = None
        self._b_open_id = None
        self._test_a = None
        self._test_b = None

    @property
    def a_open_id(self):
        return self._a_open_id

    @a_open_id.setter
    def a_open_id(self, value):
        self._a_open_id = value
    @property
    def b_open_id(self):
        return self._b_open_id

    @b_open_id.setter
    def b_open_id(self, value):
        self._b_open_id = value
    @property
    def test_a(self):
        return self._test_a

    @test_a.setter
    def test_a(self, value):
        self._test_a = value
    @property
    def test_b(self):
        return self._test_b

    @test_b.setter
    def test_b(self, value):
        self._test_b = value


    def to_alipay_dict(self):
        params = dict()
        if self.a_open_id:
            if hasattr(self.a_open_id, 'to_alipay_dict'):
                params['a_open_id'] = self.a_open_id.to_alipay_dict()
            else:
                params['a_open_id'] = self.a_open_id
        if self.b_open_id:
            if hasattr(self.b_open_id, 'to_alipay_dict'):
                params['b_open_id'] = self.b_open_id.to_alipay_dict()
            else:
                params['b_open_id'] = self.b_open_id
        if self.test_a:
            if hasattr(self.test_a, 'to_alipay_dict'):
                params['test_a'] = self.test_a.to_alipay_dict()
            else:
                params['test_a'] = self.test_a
        if self.test_b:
            if hasattr(self.test_b, 'to_alipay_dict'):
                params['test_b'] = self.test_b.to_alipay_dict()
            else:
                params['test_b'] = self.test_b
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossProdDateTestSendModel()
        if 'a_open_id' in d:
            o.a_open_id = d['a_open_id']
        if 'b_open_id' in d:
            o.b_open_id = d['b_open_id']
        if 'test_a' in d:
            o.test_a = d['test_a']
        if 'test_b' in d:
            o.test_b = d['test_b']
        return o


