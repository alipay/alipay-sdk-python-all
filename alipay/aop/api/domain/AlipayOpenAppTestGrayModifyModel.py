#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppTestGrayModifyModel(object):

    def __init__(self):
        self._a = None
        self._b = None
        self._b_param = None
        self._c = None
        self._d = None
        self._e = None
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
    def b_param(self):
        return self._b_param

    @b_param.setter
    def b_param(self, value):
        self._b_param = value
    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, value):
        self._c = value
    @property
    def d(self):
        return self._d

    @d.setter
    def d(self, value):
        self._d = value
    @property
    def e(self):
        return self._e

    @e.setter
    def e(self, value):
        self._e = value
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
        if self.b_param:
            if hasattr(self.b_param, 'to_alipay_dict'):
                params['b_param'] = self.b_param.to_alipay_dict()
            else:
                params['b_param'] = self.b_param
        if self.c:
            if hasattr(self.c, 'to_alipay_dict'):
                params['c'] = self.c.to_alipay_dict()
            else:
                params['c'] = self.c
        if self.d:
            if hasattr(self.d, 'to_alipay_dict'):
                params['d'] = self.d.to_alipay_dict()
            else:
                params['d'] = self.d
        if self.e:
            if hasattr(self.e, 'to_alipay_dict'):
                params['e'] = self.e.to_alipay_dict()
            else:
                params['e'] = self.e
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
        o = AlipayOpenAppTestGrayModifyModel()
        if 'a' in d:
            o.a = d['a']
        if 'b' in d:
            o.b = d['b']
        if 'b_param' in d:
            o.b_param = d['b_param']
        if 'c' in d:
            o.c = d['c']
        if 'd' in d:
            o.d = d['d']
        if 'e' in d:
            o.e = d['e']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


