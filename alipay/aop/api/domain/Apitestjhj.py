#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Apitestjhj(object):

    def __init__(self):
        self._para_a = None
        self._para_b = None
        self._para_c = None
        self._para_d = None
        self._para_e = None

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
    @property
    def para_e(self):
        return self._para_e

    @para_e.setter
    def para_e(self, value):
        self._para_e = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.para_e:
            if hasattr(self.para_e, 'to_alipay_dict'):
                params['para_e'] = self.para_e.to_alipay_dict()
            else:
                params['para_e'] = self.para_e
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Apitestjhj()
        if 'para_a' in d:
            o.para_a = d['para_a']
        if 'para_b' in d:
            o.para_b = d['para_b']
        if 'para_c' in d:
            o.para_c = d['para_c']
        if 'para_d' in d:
            o.para_d = d['para_d']
        if 'para_e' in d:
            o.para_e = d['para_e']
        return o


