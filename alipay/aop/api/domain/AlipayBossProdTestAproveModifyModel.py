#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PublicComplex import PublicComplex
from alipay.aop.api.domain.PublicComplex import PublicComplex


class AlipayBossProdTestAproveModifyModel(object):

    def __init__(self):
        self._complex_copy = None
        self._complex_ref = None
        self._test_a = None
        self._test_string = None
        self._test_string_open_id = None

    @property
    def complex_copy(self):
        return self._complex_copy

    @complex_copy.setter
    def complex_copy(self, value):
        if isinstance(value, PublicComplex):
            self._complex_copy = value
        else:
            self._complex_copy = PublicComplex.from_alipay_dict(value)
    @property
    def complex_ref(self):
        return self._complex_ref

    @complex_ref.setter
    def complex_ref(self, value):
        if isinstance(value, PublicComplex):
            self._complex_ref = value
        else:
            self._complex_ref = PublicComplex.from_alipay_dict(value)
    @property
    def test_a(self):
        return self._test_a

    @test_a.setter
    def test_a(self, value):
        self._test_a = value
    @property
    def test_string(self):
        return self._test_string

    @test_string.setter
    def test_string(self, value):
        self._test_string = value
    @property
    def test_string_open_id(self):
        return self._test_string_open_id

    @test_string_open_id.setter
    def test_string_open_id(self, value):
        self._test_string_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.complex_copy:
            if hasattr(self.complex_copy, 'to_alipay_dict'):
                params['complex_copy'] = self.complex_copy.to_alipay_dict()
            else:
                params['complex_copy'] = self.complex_copy
        if self.complex_ref:
            if hasattr(self.complex_ref, 'to_alipay_dict'):
                params['complex_ref'] = self.complex_ref.to_alipay_dict()
            else:
                params['complex_ref'] = self.complex_ref
        if self.test_a:
            if hasattr(self.test_a, 'to_alipay_dict'):
                params['test_a'] = self.test_a.to_alipay_dict()
            else:
                params['test_a'] = self.test_a
        if self.test_string:
            if hasattr(self.test_string, 'to_alipay_dict'):
                params['test_string'] = self.test_string.to_alipay_dict()
            else:
                params['test_string'] = self.test_string
        if self.test_string_open_id:
            if hasattr(self.test_string_open_id, 'to_alipay_dict'):
                params['test_string_open_id'] = self.test_string_open_id.to_alipay_dict()
            else:
                params['test_string_open_id'] = self.test_string_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossProdTestAproveModifyModel()
        if 'complex_copy' in d:
            o.complex_copy = d['complex_copy']
        if 'complex_ref' in d:
            o.complex_ref = d['complex_ref']
        if 'test_a' in d:
            o.test_a = d['test_a']
        if 'test_string' in d:
            o.test_string = d['test_string']
        if 'test_string_open_id' in d:
            o.test_string_open_id = d['test_string_open_id']
        return o


