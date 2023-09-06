#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PublicComplexWzw import PublicComplexWzw


class PublicComplex(object):

    def __init__(self):
        self._complex_testa = None
        self._test_boolean = None
        self._test_date = None
        self._test_new = None
        self._test_number = None
        self._test_price = None
        self._test_string = None
        self._test_string_open_id = None
        self._update_test = None

    @property
    def complex_testa(self):
        return self._complex_testa

    @complex_testa.setter
    def complex_testa(self, value):
        if isinstance(value, PublicComplexWzw):
            self._complex_testa = value
        else:
            self._complex_testa = PublicComplexWzw.from_alipay_dict(value)
    @property
    def test_boolean(self):
        return self._test_boolean

    @test_boolean.setter
    def test_boolean(self, value):
        if isinstance(value, list):
            self._test_boolean = list()
            for i in value:
                self._test_boolean.append(i)
    @property
    def test_date(self):
        return self._test_date

    @test_date.setter
    def test_date(self, value):
        self._test_date = value
    @property
    def test_new(self):
        return self._test_new

    @test_new.setter
    def test_new(self, value):
        self._test_new = value
    @property
    def test_number(self):
        return self._test_number

    @test_number.setter
    def test_number(self, value):
        if isinstance(value, list):
            self._test_number = list()
            for i in value:
                self._test_number.append(i)
    @property
    def test_price(self):
        return self._test_price

    @test_price.setter
    def test_price(self, value):
        if isinstance(value, list):
            self._test_price = list()
            for i in value:
                self._test_price.append(i)
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
    @property
    def update_test(self):
        return self._update_test

    @update_test.setter
    def update_test(self, value):
        self._update_test = value


    def to_alipay_dict(self):
        params = dict()
        if self.complex_testa:
            if hasattr(self.complex_testa, 'to_alipay_dict'):
                params['complex_testa'] = self.complex_testa.to_alipay_dict()
            else:
                params['complex_testa'] = self.complex_testa
        if self.test_boolean:
            if isinstance(self.test_boolean, list):
                for i in range(0, len(self.test_boolean)):
                    element = self.test_boolean[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.test_boolean[i] = element.to_alipay_dict()
            if hasattr(self.test_boolean, 'to_alipay_dict'):
                params['test_boolean'] = self.test_boolean.to_alipay_dict()
            else:
                params['test_boolean'] = self.test_boolean
        if self.test_date:
            if hasattr(self.test_date, 'to_alipay_dict'):
                params['test_date'] = self.test_date.to_alipay_dict()
            else:
                params['test_date'] = self.test_date
        if self.test_new:
            if hasattr(self.test_new, 'to_alipay_dict'):
                params['test_new'] = self.test_new.to_alipay_dict()
            else:
                params['test_new'] = self.test_new
        if self.test_number:
            if isinstance(self.test_number, list):
                for i in range(0, len(self.test_number)):
                    element = self.test_number[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.test_number[i] = element.to_alipay_dict()
            if hasattr(self.test_number, 'to_alipay_dict'):
                params['test_number'] = self.test_number.to_alipay_dict()
            else:
                params['test_number'] = self.test_number
        if self.test_price:
            if isinstance(self.test_price, list):
                for i in range(0, len(self.test_price)):
                    element = self.test_price[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.test_price[i] = element.to_alipay_dict()
            if hasattr(self.test_price, 'to_alipay_dict'):
                params['test_price'] = self.test_price.to_alipay_dict()
            else:
                params['test_price'] = self.test_price
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
        if self.update_test:
            if hasattr(self.update_test, 'to_alipay_dict'):
                params['update_test'] = self.update_test.to_alipay_dict()
            else:
                params['update_test'] = self.update_test
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PublicComplex()
        if 'complex_testa' in d:
            o.complex_testa = d['complex_testa']
        if 'test_boolean' in d:
            o.test_boolean = d['test_boolean']
        if 'test_date' in d:
            o.test_date = d['test_date']
        if 'test_new' in d:
            o.test_new = d['test_new']
        if 'test_number' in d:
            o.test_number = d['test_number']
        if 'test_price' in d:
            o.test_price = d['test_price']
        if 'test_string' in d:
            o.test_string = d['test_string']
        if 'test_string_open_id' in d:
            o.test_string_open_id = d['test_string_open_id']
        if 'update_test' in d:
            o.update_test = d['update_test']
        return o


