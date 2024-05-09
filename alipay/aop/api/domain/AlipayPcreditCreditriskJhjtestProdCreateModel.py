#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PublicTestProd import PublicTestProd


class AlipayPcreditCreditriskJhjtestProdCreateModel(object):

    def __init__(self):
        self._a_openid = None
        self._b_openid = None
        self._complex = None
        self._test_a = None
        self._test_b = None

    @property
    def a_openid(self):
        return self._a_openid

    @a_openid.setter
    def a_openid(self, value):
        self._a_openid = value
    @property
    def b_openid(self):
        return self._b_openid

    @b_openid.setter
    def b_openid(self, value):
        self._b_openid = value
    @property
    def complex(self):
        return self._complex

    @complex.setter
    def complex(self, value):
        if isinstance(value, PublicTestProd):
            self._complex = value
        else:
            self._complex = PublicTestProd.from_alipay_dict(value)
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
        if self.a_openid:
            if hasattr(self.a_openid, 'to_alipay_dict'):
                params['a_openid'] = self.a_openid.to_alipay_dict()
            else:
                params['a_openid'] = self.a_openid
        if self.b_openid:
            if hasattr(self.b_openid, 'to_alipay_dict'):
                params['b_openid'] = self.b_openid.to_alipay_dict()
            else:
                params['b_openid'] = self.b_openid
        if self.complex:
            if hasattr(self.complex, 'to_alipay_dict'):
                params['complex'] = self.complex.to_alipay_dict()
            else:
                params['complex'] = self.complex
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
        o = AlipayPcreditCreditriskJhjtestProdCreateModel()
        if 'a_openid' in d:
            o.a_openid = d['a_openid']
        if 'b_openid' in d:
            o.b_openid = d['b_openid']
        if 'complex' in d:
            o.complex = d['complex']
        if 'test_a' in d:
            o.test_a = d['test_a']
        if 'test_b' in d:
            o.test_b = d['test_b']
        return o


