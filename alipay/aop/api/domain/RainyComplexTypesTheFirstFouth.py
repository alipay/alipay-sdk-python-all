#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainyComplexTypesTheFirst import RainyComplexTypesTheFirst


class RainyComplexTypesTheFirstFouth(object):

    def __init__(self):
        self._fifth_level = None
        self._fouth_level_boolean = None
        self._fouth_level_num = None
        self._fouth_level_string = None
        self._new_creat = None
        self._test_a = None
        self._test_b = None

    @property
    def fifth_level(self):
        return self._fifth_level

    @fifth_level.setter
    def fifth_level(self, value):
        if isinstance(value, RainyComplexTypesTheFirst):
            self._fifth_level = value
        else:
            self._fifth_level = RainyComplexTypesTheFirst.from_alipay_dict(value)
    @property
    def fouth_level_boolean(self):
        return self._fouth_level_boolean

    @fouth_level_boolean.setter
    def fouth_level_boolean(self, value):
        self._fouth_level_boolean = value
    @property
    def fouth_level_num(self):
        return self._fouth_level_num

    @fouth_level_num.setter
    def fouth_level_num(self, value):
        self._fouth_level_num = value
    @property
    def fouth_level_string(self):
        return self._fouth_level_string

    @fouth_level_string.setter
    def fouth_level_string(self, value):
        self._fouth_level_string = value
    @property
    def new_creat(self):
        return self._new_creat

    @new_creat.setter
    def new_creat(self, value):
        self._new_creat = value
    @property
    def test_a(self):
        return self._test_a

    @test_a.setter
    def test_a(self, value):
        self._test_a = value
    @property
    def test_b(self):
        return self._test_b

    @test_b.setter
    def test_b(self, value):
        self._test_b = value


    def to_alipay_dict(self):
        params = dict()
        if self.fifth_level:
            if hasattr(self.fifth_level, 'to_alipay_dict'):
                params['fifth_level'] = self.fifth_level.to_alipay_dict()
            else:
                params['fifth_level'] = self.fifth_level
        if self.fouth_level_boolean:
            if hasattr(self.fouth_level_boolean, 'to_alipay_dict'):
                params['fouth_level_boolean'] = self.fouth_level_boolean.to_alipay_dict()
            else:
                params['fouth_level_boolean'] = self.fouth_level_boolean
        if self.fouth_level_num:
            if hasattr(self.fouth_level_num, 'to_alipay_dict'):
                params['fouth_level_num'] = self.fouth_level_num.to_alipay_dict()
            else:
                params['fouth_level_num'] = self.fouth_level_num
        if self.fouth_level_string:
            if hasattr(self.fouth_level_string, 'to_alipay_dict'):
                params['fouth_level_string'] = self.fouth_level_string.to_alipay_dict()
            else:
                params['fouth_level_string'] = self.fouth_level_string
        if self.new_creat:
            if hasattr(self.new_creat, 'to_alipay_dict'):
                params['new_creat'] = self.new_creat.to_alipay_dict()
            else:
                params['new_creat'] = self.new_creat
        if self.test_a:
            if hasattr(self.test_a, 'to_alipay_dict'):
                params['test_a'] = self.test_a.to_alipay_dict()
            else:
                params['test_a'] = self.test_a
        if self.test_b:
            if hasattr(self.test_b, 'to_alipay_dict'):
                params['test_b'] = self.test_b.to_alipay_dict()
            else:
                params['test_b'] = self.test_b
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RainyComplexTypesTheFirstFouth()
        if 'fifth_level' in d:
            o.fifth_level = d['fifth_level']
        if 'fouth_level_boolean' in d:
            o.fouth_level_boolean = d['fouth_level_boolean']
        if 'fouth_level_num' in d:
            o.fouth_level_num = d['fouth_level_num']
        if 'fouth_level_string' in d:
            o.fouth_level_string = d['fouth_level_string']
        if 'new_creat' in d:
            o.new_creat = d['new_creat']
        if 'test_a' in d:
            o.test_a = d['test_a']
        if 'test_b' in d:
            o.test_b = d['test_b']
        return o


