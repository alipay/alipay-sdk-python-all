#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PublicTestProd import PublicTestProd


class AlipayPcreditCreditriskJhjtestProdCreateModel(object):

    def __init__(self):
        self._complex = None
        self._test_a = None

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


    def to_alipay_dict(self):
        params = dict()
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditCreditriskJhjtestProdCreateModel()
        if 'complex' in d:
            o.complex = d['complex']
        if 'test_a' in d:
            o.test_a = d['test_a']
        return o


