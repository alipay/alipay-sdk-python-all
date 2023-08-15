#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CorporateSealRectOpenVO import CorporateSealRectOpenVO


class PublicComplexWzw(object):

    def __init__(self):
        self._complex_a = None
        self._test_boolean = None
        self._test_number = None
        self._test_string = None
        self._test_string_open_id = None

    @property
    def complex_a(self):
        return self._complex_a

    @complex_a.setter
    def complex_a(self, value):
        if isinstance(value, CorporateSealRectOpenVO):
            self._complex_a = value
        else:
            self._complex_a = CorporateSealRectOpenVO.from_alipay_dict(value)
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
    def test_number(self):
        return self._test_number

    @test_number.setter
    def test_number(self, value):
        if isinstance(value, list):
            self._test_number = list()
            for i in value:
                self._test_number.append(i)
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
        if self.complex_a:
            if hasattr(self.complex_a, 'to_alipay_dict'):
                params['complex_a'] = self.complex_a.to_alipay_dict()
            else:
                params['complex_a'] = self.complex_a
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
        o = PublicComplexWzw()
        if 'complex_a' in d:
            o.complex_a = d['complex_a']
        if 'test_boolean' in d:
            o.test_boolean = d['test_boolean']
        if 'test_number' in d:
            o.test_number = d['test_number']
        if 'test_string' in d:
            o.test_string = d['test_string']
        if 'test_string_open_id' in d:
            o.test_string_open_id = d['test_string_open_id']
        return o


