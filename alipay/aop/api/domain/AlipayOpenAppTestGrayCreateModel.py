#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenidComplex import OpenidComplex


class AlipayOpenAppTestGrayCreateModel(object):

    def __init__(self):
        self._a = None
        self._b = None
        self._body = None
        self._body_1 = None
        self._c = None
        self._complex_param = None
        self._oid = None
        self._open_id = None
        self._user_id = None

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
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        self._body = value
    @property
    def body_1(self):
        return self._body_1

    @body_1.setter
    def body_1(self, value):
        self._body_1 = value
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
    def oid(self):
        return self._oid

    @oid.setter
    def oid(self, value):
        self._oid = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


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
        if self.body:
            if hasattr(self.body, 'to_alipay_dict'):
                params['body'] = self.body.to_alipay_dict()
            else:
                params['body'] = self.body
        if self.body_1:
            if hasattr(self.body_1, 'to_alipay_dict'):
                params['body_1'] = self.body_1.to_alipay_dict()
            else:
                params['body_1'] = self.body_1
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
        if self.oid:
            if hasattr(self.oid, 'to_alipay_dict'):
                params['oid'] = self.oid.to_alipay_dict()
            else:
                params['oid'] = self.oid
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppTestGrayCreateModel()
        if 'a' in d:
            o.a = d['a']
        if 'b' in d:
            o.b = d['b']
        if 'body' in d:
            o.body = d['body']
        if 'body_1' in d:
            o.body_1 = d['body_1']
        if 'c' in d:
            o.c = d['c']
        if 'complex_param' in d:
            o.complex_param = d['complex_param']
        if 'oid' in d:
            o.oid = d['oid']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


