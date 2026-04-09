#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainyComplexTypesTheFirstFouth import RainyComplexTypesTheFirstFouth


class RainyComplexTypesTheFirstThree(object):

    def __init__(self):
        self._fouth_level = None
        self._new_creat = None
        self._test_a = None
        self._test_b = None

    @property
    def fouth_level(self):
        return self._fouth_level

    @fouth_level.setter
    def fouth_level(self, value):
        if isinstance(value, RainyComplexTypesTheFirstFouth):
            self._fouth_level = value
        else:
            self._fouth_level = RainyComplexTypesTheFirstFouth.from_alipay_dict(value)
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
        if self.fouth_level:
            if hasattr(self.fouth_level, 'to_alipay_dict'):
                params['fouth_level'] = self.fouth_level.to_alipay_dict()
            else:
                params['fouth_level'] = self.fouth_level
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
        o = RainyComplexTypesTheFirstThree()
        if 'fouth_level' in d:
            o.fouth_level = d['fouth_level']
        if 'new_creat' in d:
            o.new_creat = d['new_creat']
        if 'test_a' in d:
            o.test_a = d['test_a']
        if 'test_b' in d:
            o.test_b = d['test_b']
        return o


