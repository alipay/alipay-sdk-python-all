#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PublicComplex import PublicComplex


class AlipayDataDataserviceDataJhjtestQueryModel(object):

    def __init__(self):
        self._inner = None
        self._input_a = None
        self._input_b = None
        self._input_c = None
        self._input_c_yincang = None
        self._input_complex_a = None
        self._input_d = None
        self._input_e = None
        self._open_id = None
        self._uid = None

    @property
    def inner(self):
        return self._inner

    @inner.setter
    def inner(self, value):
        self._inner = value
    @property
    def input_a(self):
        return self._input_a

    @input_a.setter
    def input_a(self, value):
        self._input_a = value
    @property
    def input_b(self):
        return self._input_b

    @input_b.setter
    def input_b(self, value):
        self._input_b = value
    @property
    def input_c(self):
        return self._input_c

    @input_c.setter
    def input_c(self, value):
        self._input_c = value
    @property
    def input_c_yincang(self):
        return self._input_c_yincang

    @input_c_yincang.setter
    def input_c_yincang(self, value):
        self._input_c_yincang = value
    @property
    def input_complex_a(self):
        return self._input_complex_a

    @input_complex_a.setter
    def input_complex_a(self, value):
        if isinstance(value, PublicComplex):
            self._input_complex_a = value
        else:
            self._input_complex_a = PublicComplex.from_alipay_dict(value)
    @property
    def input_d(self):
        return self._input_d

    @input_d.setter
    def input_d(self, value):
        self._input_d = value
    @property
    def input_e(self):
        return self._input_e

    @input_e.setter
    def input_e(self, value):
        self._input_e = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.inner:
            if hasattr(self.inner, 'to_alipay_dict'):
                params['inner'] = self.inner.to_alipay_dict()
            else:
                params['inner'] = self.inner
        if self.input_a:
            if hasattr(self.input_a, 'to_alipay_dict'):
                params['input_a'] = self.input_a.to_alipay_dict()
            else:
                params['input_a'] = self.input_a
        if self.input_b:
            if hasattr(self.input_b, 'to_alipay_dict'):
                params['input_b'] = self.input_b.to_alipay_dict()
            else:
                params['input_b'] = self.input_b
        if self.input_c:
            if hasattr(self.input_c, 'to_alipay_dict'):
                params['input_c'] = self.input_c.to_alipay_dict()
            else:
                params['input_c'] = self.input_c
        if self.input_c_yincang:
            if hasattr(self.input_c_yincang, 'to_alipay_dict'):
                params['input_c_yincang'] = self.input_c_yincang.to_alipay_dict()
            else:
                params['input_c_yincang'] = self.input_c_yincang
        if self.input_complex_a:
            if hasattr(self.input_complex_a, 'to_alipay_dict'):
                params['input_complex_a'] = self.input_complex_a.to_alipay_dict()
            else:
                params['input_complex_a'] = self.input_complex_a
        if self.input_d:
            if hasattr(self.input_d, 'to_alipay_dict'):
                params['input_d'] = self.input_d.to_alipay_dict()
            else:
                params['input_d'] = self.input_d
        if self.input_e:
            if hasattr(self.input_e, 'to_alipay_dict'):
                params['input_e'] = self.input_e.to_alipay_dict()
            else:
                params['input_e'] = self.input_e
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceDataJhjtestQueryModel()
        if 'inner' in d:
            o.inner = d['inner']
        if 'input_a' in d:
            o.input_a = d['input_a']
        if 'input_b' in d:
            o.input_b = d['input_b']
        if 'input_c' in d:
            o.input_c = d['input_c']
        if 'input_c_yincang' in d:
            o.input_c_yincang = d['input_c_yincang']
        if 'input_complex_a' in d:
            o.input_complex_a = d['input_complex_a']
        if 'input_d' in d:
            o.input_d = d['input_d']
        if 'input_e' in d:
            o.input_e = d['input_e']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'uid' in d:
            o.uid = d['uid']
        return o


