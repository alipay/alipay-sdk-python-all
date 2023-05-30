#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TestDemo import TestDemo


class AlipayIsponetestWzwtestWzwtestQueryModel(object):

    def __init__(self):
        self._a_open_id = None
        self._aaaa = None
        self._bbbb = None
        self._ccc = None
        self._complex_a = None
        self._complex_b = None
        self._string_a = None
        self._string_b = None
        self._uid_a = None

    @property
    def a_open_id(self):
        return self._a_open_id

    @a_open_id.setter
    def a_open_id(self, value):
        self._a_open_id = value
    @property
    def aaaa(self):
        return self._aaaa

    @aaaa.setter
    def aaaa(self, value):
        self._aaaa = value
    @property
    def bbbb(self):
        return self._bbbb

    @bbbb.setter
    def bbbb(self, value):
        self._bbbb = value
    @property
    def ccc(self):
        return self._ccc

    @ccc.setter
    def ccc(self, value):
        self._ccc = value
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
        self._complex_b = value
    @property
    def string_a(self):
        return self._string_a

    @string_a.setter
    def string_a(self, value):
        self._string_a = value
    @property
    def string_b(self):
        return self._string_b

    @string_b.setter
    def string_b(self, value):
        self._string_b = value
    @property
    def uid_a(self):
        return self._uid_a

    @uid_a.setter
    def uid_a(self, value):
        self._uid_a = value


    def to_alipay_dict(self):
        params = dict()
        if self.a_open_id:
            if hasattr(self.a_open_id, 'to_alipay_dict'):
                params['a_open_id'] = self.a_open_id.to_alipay_dict()
            else:
                params['a_open_id'] = self.a_open_id
        if self.aaaa:
            if hasattr(self.aaaa, 'to_alipay_dict'):
                params['aaaa'] = self.aaaa.to_alipay_dict()
            else:
                params['aaaa'] = self.aaaa
        if self.bbbb:
            if hasattr(self.bbbb, 'to_alipay_dict'):
                params['bbbb'] = self.bbbb.to_alipay_dict()
            else:
                params['bbbb'] = self.bbbb
        if self.ccc:
            if hasattr(self.ccc, 'to_alipay_dict'):
                params['ccc'] = self.ccc.to_alipay_dict()
            else:
                params['ccc'] = self.ccc
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
        if self.string_a:
            if hasattr(self.string_a, 'to_alipay_dict'):
                params['string_a'] = self.string_a.to_alipay_dict()
            else:
                params['string_a'] = self.string_a
        if self.string_b:
            if hasattr(self.string_b, 'to_alipay_dict'):
                params['string_b'] = self.string_b.to_alipay_dict()
            else:
                params['string_b'] = self.string_b
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
        o = AlipayIsponetestWzwtestWzwtestQueryModel()
        if 'a_open_id' in d:
            o.a_open_id = d['a_open_id']
        if 'aaaa' in d:
            o.aaaa = d['aaaa']
        if 'bbbb' in d:
            o.bbbb = d['bbbb']
        if 'ccc' in d:
            o.ccc = d['ccc']
        if 'complex_a' in d:
            o.complex_a = d['complex_a']
        if 'complex_b' in d:
            o.complex_b = d['complex_b']
        if 'string_a' in d:
            o.string_a = d['string_a']
        if 'string_b' in d:
            o.string_b = d['string_b']
        if 'uid_a' in d:
            o.uid_a = d['uid_a']
        return o


