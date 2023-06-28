#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MlmParamTest(object):

    def __init__(self):
        self._param_mlm_a = None
        self._param_mlm_b = None
        self._param_mlm_c = None
        self._param_mlm_d = None
        self._param_mlm_e = None

    @property
    def param_mlm_a(self):
        return self._param_mlm_a

    @param_mlm_a.setter
    def param_mlm_a(self, value):
        self._param_mlm_a = value
    @property
    def param_mlm_b(self):
        return self._param_mlm_b

    @param_mlm_b.setter
    def param_mlm_b(self, value):
        self._param_mlm_b = value
    @property
    def param_mlm_c(self):
        return self._param_mlm_c

    @param_mlm_c.setter
    def param_mlm_c(self, value):
        self._param_mlm_c = value
    @property
    def param_mlm_d(self):
        return self._param_mlm_d

    @param_mlm_d.setter
    def param_mlm_d(self, value):
        self._param_mlm_d = value
    @property
    def param_mlm_e(self):
        return self._param_mlm_e

    @param_mlm_e.setter
    def param_mlm_e(self, value):
        self._param_mlm_e = value


    def to_alipay_dict(self):
        params = dict()
        if self.param_mlm_a:
            if hasattr(self.param_mlm_a, 'to_alipay_dict'):
                params['param_mlm_a'] = self.param_mlm_a.to_alipay_dict()
            else:
                params['param_mlm_a'] = self.param_mlm_a
        if self.param_mlm_b:
            if hasattr(self.param_mlm_b, 'to_alipay_dict'):
                params['param_mlm_b'] = self.param_mlm_b.to_alipay_dict()
            else:
                params['param_mlm_b'] = self.param_mlm_b
        if self.param_mlm_c:
            if hasattr(self.param_mlm_c, 'to_alipay_dict'):
                params['param_mlm_c'] = self.param_mlm_c.to_alipay_dict()
            else:
                params['param_mlm_c'] = self.param_mlm_c
        if self.param_mlm_d:
            if hasattr(self.param_mlm_d, 'to_alipay_dict'):
                params['param_mlm_d'] = self.param_mlm_d.to_alipay_dict()
            else:
                params['param_mlm_d'] = self.param_mlm_d
        if self.param_mlm_e:
            if hasattr(self.param_mlm_e, 'to_alipay_dict'):
                params['param_mlm_e'] = self.param_mlm_e.to_alipay_dict()
            else:
                params['param_mlm_e'] = self.param_mlm_e
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MlmParamTest()
        if 'param_mlm_a' in d:
            o.param_mlm_a = d['param_mlm_a']
        if 'param_mlm_b' in d:
            o.param_mlm_b = d['param_mlm_b']
        if 'param_mlm_c' in d:
            o.param_mlm_c = d['param_mlm_c']
        if 'param_mlm_d' in d:
            o.param_mlm_d = d['param_mlm_d']
        if 'param_mlm_e' in d:
            o.param_mlm_e = d['param_mlm_e']
        return o


