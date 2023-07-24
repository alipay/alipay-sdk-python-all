#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PublicComplex import PublicComplex
from alipay.aop.api.domain.PublicComplexWzw import PublicComplexWzw
from alipay.aop.api.domain.PublicComplex import PublicComplex


class AlipayBossProdTestModifyModel(object):

    def __init__(self):
        self._complex_copy = None
        self._complex_copy_2 = None
        self._complex_ref = None
        self._test_a = None
        self._test_boolean = None
        self._test_date = None
        self._test_number = None
        self._test_price = None
        self._test_string = None

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
    def complex_copy_2(self):
        return self._complex_copy_2

    @complex_copy_2.setter
    def complex_copy_2(self, value):
        if isinstance(value, PublicComplexWzw):
            self._complex_copy_2 = value
        else:
            self._complex_copy_2 = PublicComplexWzw.from_alipay_dict(value)
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
    def test_boolean(self):
        return self._test_boolean

    @test_boolean.setter
    def test_boolean(self, value):
        self._test_boolean = value
    @property
    def test_date(self):
        return self._test_date

    @test_date.setter
    def test_date(self, value):
        self._test_date = value
    @property
    def test_number(self):
        return self._test_number

    @test_number.setter
    def test_number(self, value):
        self._test_number = value
    @property
    def test_price(self):
        return self._test_price

    @test_price.setter
    def test_price(self, value):
        self._test_price = value
    @property
    def test_string(self):
        return self._test_string

    @test_string.setter
    def test_string(self, value):
        self._test_string = value


    def to_alipay_dict(self):
        params = dict()
        if self.complex_copy:
            if hasattr(self.complex_copy, 'to_alipay_dict'):
                params['complex_copy'] = self.complex_copy.to_alipay_dict()
            else:
                params['complex_copy'] = self.complex_copy
        if self.complex_copy_2:
            if hasattr(self.complex_copy_2, 'to_alipay_dict'):
                params['complex_copy_2'] = self.complex_copy_2.to_alipay_dict()
            else:
                params['complex_copy_2'] = self.complex_copy_2
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
        if self.test_boolean:
            if hasattr(self.test_boolean, 'to_alipay_dict'):
                params['test_boolean'] = self.test_boolean.to_alipay_dict()
            else:
                params['test_boolean'] = self.test_boolean
        if self.test_date:
            if hasattr(self.test_date, 'to_alipay_dict'):
                params['test_date'] = self.test_date.to_alipay_dict()
            else:
                params['test_date'] = self.test_date
        if self.test_number:
            if hasattr(self.test_number, 'to_alipay_dict'):
                params['test_number'] = self.test_number.to_alipay_dict()
            else:
                params['test_number'] = self.test_number
        if self.test_price:
            if hasattr(self.test_price, 'to_alipay_dict'):
                params['test_price'] = self.test_price.to_alipay_dict()
            else:
                params['test_price'] = self.test_price
        if self.test_string:
            if hasattr(self.test_string, 'to_alipay_dict'):
                params['test_string'] = self.test_string.to_alipay_dict()
            else:
                params['test_string'] = self.test_string
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossProdTestModifyModel()
        if 'complex_copy' in d:
            o.complex_copy = d['complex_copy']
        if 'complex_copy_2' in d:
            o.complex_copy_2 = d['complex_copy_2']
        if 'complex_ref' in d:
            o.complex_ref = d['complex_ref']
        if 'test_a' in d:
            o.test_a = d['test_a']
        if 'test_boolean' in d:
            o.test_boolean = d['test_boolean']
        if 'test_date' in d:
            o.test_date = d['test_date']
        if 'test_number' in d:
            o.test_number = d['test_number']
        if 'test_price' in d:
            o.test_price = d['test_price']
        if 'test_string' in d:
            o.test_string = d['test_string']
        return o


