#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApiScheameTwo import ApiScheameTwo


class ApiScheameOne(object):

    def __init__(self):
        self._test_a = None
        self._test_b = None

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
        if isinstance(value, list):
            self._test_b = list()
            for i in value:
                if isinstance(i, ApiScheameTwo):
                    self._test_b.append(i)
                else:
                    self._test_b.append(ApiScheameTwo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.test_a:
            if hasattr(self.test_a, 'to_alipay_dict'):
                params['test_a'] = self.test_a.to_alipay_dict()
            else:
                params['test_a'] = self.test_a
        if self.test_b:
            if isinstance(self.test_b, list):
                for i in range(0, len(self.test_b)):
                    element = self.test_b[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.test_b[i] = element.to_alipay_dict()
            if hasattr(self.test_b, 'to_alipay_dict'):
                params['test_b'] = self.test_b.to_alipay_dict()
            else:
                params['test_b'] = self.test_b
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApiScheameOne()
        if 'test_a' in d:
            o.test_a = d['test_a']
        if 'test_b' in d:
            o.test_b = d['test_b']
        return o


