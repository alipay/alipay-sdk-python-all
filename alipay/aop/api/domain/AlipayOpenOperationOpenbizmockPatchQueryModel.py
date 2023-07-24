#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TestDemo import TestDemo
from alipay.aop.api.domain.TestDemo import TestDemo
from alipay.aop.api.domain.TestDemoWzw import TestDemoWzw
from alipay.aop.api.domain.TestDemoWzw import TestDemoWzw


class AlipayOpenOperationOpenbizmockPatchQueryModel(object):

    def __init__(self):
        self._b_query = None
        self._c_body = None
        self._complex_a = None
        self._complex_b = None
        self._complex_c = None
        self._complex_d = None
        self._id_type_modify_open_id = None
        self._id_typea = None
        self._price = None
        self._uida = None

    @property
    def b_query(self):
        return self._b_query

    @b_query.setter
    def b_query(self, value):
        self._b_query = value
    @property
    def c_body(self):
        return self._c_body

    @c_body.setter
    def c_body(self, value):
        self._c_body = value
    @property
    def complex_a(self):
        return self._complex_a

    @complex_a.setter
    def complex_a(self, value):
        if isinstance(value, TestDemo):
            self._complex_a = value
        else:
            self._complex_a = TestDemo.from_alipay_dict(value)
    @property
    def complex_b(self):
        return self._complex_b

    @complex_b.setter
    def complex_b(self, value):
        if isinstance(value, TestDemo):
            self._complex_b = value
        else:
            self._complex_b = TestDemo.from_alipay_dict(value)
    @property
    def complex_c(self):
        return self._complex_c

    @complex_c.setter
    def complex_c(self, value):
        if isinstance(value, TestDemoWzw):
            self._complex_c = value
        else:
            self._complex_c = TestDemoWzw.from_alipay_dict(value)
    @property
    def complex_d(self):
        return self._complex_d

    @complex_d.setter
    def complex_d(self, value):
        if isinstance(value, TestDemoWzw):
            self._complex_d = value
        else:
            self._complex_d = TestDemoWzw.from_alipay_dict(value)
    @property
    def id_type_modify_open_id(self):
        return self._id_type_modify_open_id

    @id_type_modify_open_id.setter
    def id_type_modify_open_id(self, value):
        self._id_type_modify_open_id = value
    @property
    def id_typea(self):
        return self._id_typea

    @id_typea.setter
    def id_typea(self, value):
        self._id_typea = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def uida(self):
        return self._uida

    @uida.setter
    def uida(self, value):
        self._uida = value


    def to_alipay_dict(self):
        params = dict()
        if self.b_query:
            if hasattr(self.b_query, 'to_alipay_dict'):
                params['b_query'] = self.b_query.to_alipay_dict()
            else:
                params['b_query'] = self.b_query
        if self.c_body:
            if hasattr(self.c_body, 'to_alipay_dict'):
                params['c_body'] = self.c_body.to_alipay_dict()
            else:
                params['c_body'] = self.c_body
        if self.complex_a:
            if hasattr(self.complex_a, 'to_alipay_dict'):
                params['complex_a'] = self.complex_a.to_alipay_dict()
            else:
                params['complex_a'] = self.complex_a
        if self.complex_b:
            if hasattr(self.complex_b, 'to_alipay_dict'):
                params['complex_b'] = self.complex_b.to_alipay_dict()
            else:
                params['complex_b'] = self.complex_b
        if self.complex_c:
            if hasattr(self.complex_c, 'to_alipay_dict'):
                params['complex_c'] = self.complex_c.to_alipay_dict()
            else:
                params['complex_c'] = self.complex_c
        if self.complex_d:
            if hasattr(self.complex_d, 'to_alipay_dict'):
                params['complex_d'] = self.complex_d.to_alipay_dict()
            else:
                params['complex_d'] = self.complex_d
        if self.id_type_modify_open_id:
            if hasattr(self.id_type_modify_open_id, 'to_alipay_dict'):
                params['id_type_modify_open_id'] = self.id_type_modify_open_id.to_alipay_dict()
            else:
                params['id_type_modify_open_id'] = self.id_type_modify_open_id
        if self.id_typea:
            if hasattr(self.id_typea, 'to_alipay_dict'):
                params['id_typea'] = self.id_typea.to_alipay_dict()
            else:
                params['id_typea'] = self.id_typea
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.uida:
            if hasattr(self.uida, 'to_alipay_dict'):
                params['uida'] = self.uida.to_alipay_dict()
            else:
                params['uida'] = self.uida
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOperationOpenbizmockPatchQueryModel()
        if 'b_query' in d:
            o.b_query = d['b_query']
        if 'c_body' in d:
            o.c_body = d['c_body']
        if 'complex_a' in d:
            o.complex_a = d['complex_a']
        if 'complex_b' in d:
            o.complex_b = d['complex_b']
        if 'complex_c' in d:
            o.complex_c = d['complex_c']
        if 'complex_d' in d:
            o.complex_d = d['complex_d']
        if 'id_type_modify_open_id' in d:
            o.id_type_modify_open_id = d['id_type_modify_open_id']
        if 'id_typea' in d:
            o.id_typea = d['id_typea']
        if 'price' in d:
            o.price = d['price']
        if 'uida' in d:
            o.uida = d['uida']
        return o


