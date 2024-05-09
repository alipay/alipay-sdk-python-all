#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RegressionPublic import RegressionPublic


class JhjtestDoc(object):

    def __init__(self):
        self._a_open_id = None
        self._com_a = None
        self._para_a = None
        self._para_b = None
        self._para_c = None
        self._para_d = None

    @property
    def a_open_id(self):
        return self._a_open_id

    @a_open_id.setter
    def a_open_id(self, value):
        self._a_open_id = value
    @property
    def com_a(self):
        return self._com_a

    @com_a.setter
    def com_a(self, value):
        if isinstance(value, RegressionPublic):
            self._com_a = value
        else:
            self._com_a = RegressionPublic.from_alipay_dict(value)
    @property
    def para_a(self):
        return self._para_a

    @para_a.setter
    def para_a(self, value):
        self._para_a = value
    @property
    def para_b(self):
        return self._para_b

    @para_b.setter
    def para_b(self, value):
        self._para_b = value
    @property
    def para_c(self):
        return self._para_c

    @para_c.setter
    def para_c(self, value):
        self._para_c = value
    @property
    def para_d(self):
        return self._para_d

    @para_d.setter
    def para_d(self, value):
        self._para_d = value


    def to_alipay_dict(self):
        params = dict()
        if self.a_open_id:
            if hasattr(self.a_open_id, 'to_alipay_dict'):
                params['a_open_id'] = self.a_open_id.to_alipay_dict()
            else:
                params['a_open_id'] = self.a_open_id
        if self.com_a:
            if hasattr(self.com_a, 'to_alipay_dict'):
                params['com_a'] = self.com_a.to_alipay_dict()
            else:
                params['com_a'] = self.com_a
        if self.para_a:
            if hasattr(self.para_a, 'to_alipay_dict'):
                params['para_a'] = self.para_a.to_alipay_dict()
            else:
                params['para_a'] = self.para_a
        if self.para_b:
            if hasattr(self.para_b, 'to_alipay_dict'):
                params['para_b'] = self.para_b.to_alipay_dict()
            else:
                params['para_b'] = self.para_b
        if self.para_c:
            if hasattr(self.para_c, 'to_alipay_dict'):
                params['para_c'] = self.para_c.to_alipay_dict()
            else:
                params['para_c'] = self.para_c
        if self.para_d:
            if hasattr(self.para_d, 'to_alipay_dict'):
                params['para_d'] = self.para_d.to_alipay_dict()
            else:
                params['para_d'] = self.para_d
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = JhjtestDoc()
        if 'a_open_id' in d:
            o.a_open_id = d['a_open_id']
        if 'com_a' in d:
            o.com_a = d['com_a']
        if 'para_a' in d:
            o.para_a = d['para_a']
        if 'para_b' in d:
            o.para_b = d['para_b']
        if 'para_c' in d:
            o.para_c = d['para_c']
        if 'para_d' in d:
            o.para_d = d['para_d']
        return o


