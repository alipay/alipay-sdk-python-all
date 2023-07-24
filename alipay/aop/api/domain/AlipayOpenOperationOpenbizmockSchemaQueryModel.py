#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TestDemo import TestDemo
from alipay.aop.api.domain.TestDemoWzw import TestDemoWzw


class AlipayOpenOperationOpenbizmockSchemaQueryModel(object):

    def __init__(self):
        self._a = None
        self._b = None
        self._c = None
        self._complex_a = None
        self._fuza = None
        self._id_type = None
        self._open_id = None
        self._uid = None
        self._uid_a = None

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
    def complex_a(self):
        return self._complex_a

    @complex_a.setter
    def complex_a(self, value):
        if isinstance(value, TestDemo):
            self._complex_a = value
        else:
            self._complex_a = TestDemo.from_alipay_dict(value)
    @property
    def fuza(self):
        return self._fuza

    @fuza.setter
    def fuza(self, value):
        if isinstance(value, TestDemoWzw):
            self._fuza = value
        else:
            self._fuza = TestDemoWzw.from_alipay_dict(value)
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
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value
    @property
    def uid_a(self):
        return self._uid_a

    @uid_a.setter
    def uid_a(self, value):
        self._uid_a = value


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
        if self.complex_a:
            if hasattr(self.complex_a, 'to_alipay_dict'):
                params['complex_a'] = self.complex_a.to_alipay_dict()
            else:
                params['complex_a'] = self.complex_a
        if self.fuza:
            if hasattr(self.fuza, 'to_alipay_dict'):
                params['fuza'] = self.fuza.to_alipay_dict()
            else:
                params['fuza'] = self.fuza
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
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        if self.uid_a:
            if hasattr(self.uid_a, 'to_alipay_dict'):
                params['uid_a'] = self.uid_a.to_alipay_dict()
            else:
                params['uid_a'] = self.uid_a
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOperationOpenbizmockSchemaQueryModel()
        if 'a' in d:
            o.a = d['a']
        if 'b' in d:
            o.b = d['b']
        if 'c' in d:
            o.c = d['c']
        if 'complex_a' in d:
            o.complex_a = d['complex_a']
        if 'fuza' in d:
            o.fuza = d['fuza']
        if 'id_type' in d:
            o.id_type = d['id_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'uid' in d:
            o.uid = d['uid']
        if 'uid_a' in d:
            o.uid_a = d['uid_a']
        return o


