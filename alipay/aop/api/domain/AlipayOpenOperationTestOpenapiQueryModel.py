#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenOperationTestOpenapiQueryModel(object):

    def __init__(self):
        self._id_type = None
        self._open_id = None
        self._price_a = None
        self._test_b = None
        self._test_c = None
        self._u_test = None

    @property
    def id_type(self):
        return self._id_type

    @id_type.setter
    def id_type(self, value):
        self._id_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def price_a(self):
        return self._price_a

    @price_a.setter
    def price_a(self, value):
        self._price_a = value
    @property
    def test_b(self):
        return self._test_b

    @test_b.setter
    def test_b(self, value):
        self._test_b = value
    @property
    def test_c(self):
        return self._test_c

    @test_c.setter
    def test_c(self, value):
        self._test_c = value
    @property
    def u_test(self):
        return self._u_test

    @u_test.setter
    def u_test(self, value):
        self._u_test = value


    def to_alipay_dict(self):
        params = dict()
        if self.id_type:
            if hasattr(self.id_type, 'to_alipay_dict'):
                params['id_type'] = self.id_type.to_alipay_dict()
            else:
                params['id_type'] = self.id_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.price_a:
            if hasattr(self.price_a, 'to_alipay_dict'):
                params['price_a'] = self.price_a.to_alipay_dict()
            else:
                params['price_a'] = self.price_a
        if self.test_b:
            if hasattr(self.test_b, 'to_alipay_dict'):
                params['test_b'] = self.test_b.to_alipay_dict()
            else:
                params['test_b'] = self.test_b
        if self.test_c:
            if hasattr(self.test_c, 'to_alipay_dict'):
                params['test_c'] = self.test_c.to_alipay_dict()
            else:
                params['test_c'] = self.test_c
        if self.u_test:
            if hasattr(self.u_test, 'to_alipay_dict'):
                params['u_test'] = self.u_test.to_alipay_dict()
            else:
                params['u_test'] = self.u_test
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOperationTestOpenapiQueryModel()
        if 'id_type' in d:
            o.id_type = d['id_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'price_a' in d:
            o.price_a = d['price_a']
        if 'test_b' in d:
            o.test_b = d['test_b']
        if 'test_c' in d:
            o.test_c = d['test_c']
        if 'u_test' in d:
            o.u_test = d['u_test']
        return o


