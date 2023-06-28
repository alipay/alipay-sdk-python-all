#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AAAAAtest(object):

    def __init__(self):
        self._a = None
        self._a_openid = None
        self._b = None
        self._b_openid = None
        self._e = None

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value
    @property
    def a_openid(self):
        return self._a_openid

    @a_openid.setter
    def a_openid(self, value):
        self._a_openid = value
    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = value
    @property
    def b_openid(self):
        return self._b_openid

    @b_openid.setter
    def b_openid(self, value):
        self._b_openid = value
    @property
    def e(self):
        return self._e

    @e.setter
    def e(self, value):
        self._e = value


    def to_alipay_dict(self):
        params = dict()
        if self.a:
            if hasattr(self.a, 'to_alipay_dict'):
                params['a'] = self.a.to_alipay_dict()
            else:
                params['a'] = self.a
        if self.a_openid:
            if hasattr(self.a_openid, 'to_alipay_dict'):
                params['a_openid'] = self.a_openid.to_alipay_dict()
            else:
                params['a_openid'] = self.a_openid
        if self.b:
            if hasattr(self.b, 'to_alipay_dict'):
                params['b'] = self.b.to_alipay_dict()
            else:
                params['b'] = self.b
        if self.b_openid:
            if hasattr(self.b_openid, 'to_alipay_dict'):
                params['b_openid'] = self.b_openid.to_alipay_dict()
            else:
                params['b_openid'] = self.b_openid
        if self.e:
            if hasattr(self.e, 'to_alipay_dict'):
                params['e'] = self.e.to_alipay_dict()
            else:
                params['e'] = self.e
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AAAAAtest()
        if 'a' in d:
            o.a = d['a']
        if 'a_openid' in d:
            o.a_openid = d['a_openid']
        if 'b' in d:
            o.b = d['b']
        if 'b_openid' in d:
            o.b_openid = d['b_openid']
        if 'e' in d:
            o.e = d['e']
        return o


