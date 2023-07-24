#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PublicComplex import PublicComplex
from alipay.aop.api.domain.PublicComplex import PublicComplex


class AlipayBossProdTestAproveQueryModel(object):

    def __init__(self):
        self._complex_a = None
        self._complex_b = None
        self._test_open_id = None
        self._test_uid = None

    @property
    def complex_a(self):
        return self._complex_a

    @complex_a.setter
    def complex_a(self, value):
        if isinstance(value, PublicComplex):
            self._complex_a = value
        else:
            self._complex_a = PublicComplex.from_alipay_dict(value)
    @property
    def complex_b(self):
        return self._complex_b

    @complex_b.setter
    def complex_b(self, value):
        if isinstance(value, PublicComplex):
            self._complex_b = value
        else:
            self._complex_b = PublicComplex.from_alipay_dict(value)
    @property
    def test_open_id(self):
        return self._test_open_id

    @test_open_id.setter
    def test_open_id(self, value):
        self._test_open_id = value
    @property
    def test_uid(self):
        return self._test_uid

    @test_uid.setter
    def test_uid(self, value):
        self._test_uid = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.test_open_id:
            if hasattr(self.test_open_id, 'to_alipay_dict'):
                params['test_open_id'] = self.test_open_id.to_alipay_dict()
            else:
                params['test_open_id'] = self.test_open_id
        if self.test_uid:
            if hasattr(self.test_uid, 'to_alipay_dict'):
                params['test_uid'] = self.test_uid.to_alipay_dict()
            else:
                params['test_uid'] = self.test_uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossProdTestAproveQueryModel()
        if 'complex_a' in d:
            o.complex_a = d['complex_a']
        if 'complex_b' in d:
            o.complex_b = d['complex_b']
        if 'test_open_id' in d:
            o.test_open_id = d['test_open_id']
        if 'test_uid' in d:
            o.test_uid = d['test_uid']
        return o


