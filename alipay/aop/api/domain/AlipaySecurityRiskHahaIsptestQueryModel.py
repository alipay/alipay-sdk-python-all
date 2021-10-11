#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsurancePeriod import InsurancePeriod
from alipay.aop.api.domain.RecomProduct import RecomProduct


class AlipaySecurityRiskHahaIsptestQueryModel(object):

    def __init__(self):
        self._test_five = None
        self._test_four = None
        self._test_one = None
        self._test_three = None
        self._test_two = None

    @property
    def test_five(self):
        return self._test_five

    @test_five.setter
    def test_five(self, value):
        if isinstance(value, InsurancePeriod):
            self._test_five = value
        else:
            self._test_five = InsurancePeriod.from_alipay_dict(value)
    @property
    def test_four(self):
        return self._test_four

    @test_four.setter
    def test_four(self, value):
        if isinstance(value, RecomProduct):
            self._test_four = value
        else:
            self._test_four = RecomProduct.from_alipay_dict(value)
    @property
    def test_one(self):
        return self._test_one

    @test_one.setter
    def test_one(self, value):
        self._test_one = value
    @property
    def test_three(self):
        return self._test_three

    @test_three.setter
    def test_three(self, value):
        if isinstance(value, list):
            self._test_three = list()
            for i in value:
                self._test_three.append(i)
    @property
    def test_two(self):
        return self._test_two

    @test_two.setter
    def test_two(self, value):
        self._test_two = value


    def to_alipay_dict(self):
        params = dict()
        if self.test_five:
            if hasattr(self.test_five, 'to_alipay_dict'):
                params['test_five'] = self.test_five.to_alipay_dict()
            else:
                params['test_five'] = self.test_five
        if self.test_four:
            if hasattr(self.test_four, 'to_alipay_dict'):
                params['test_four'] = self.test_four.to_alipay_dict()
            else:
                params['test_four'] = self.test_four
        if self.test_one:
            if hasattr(self.test_one, 'to_alipay_dict'):
                params['test_one'] = self.test_one.to_alipay_dict()
            else:
                params['test_one'] = self.test_one
        if self.test_three:
            if isinstance(self.test_three, list):
                for i in range(0, len(self.test_three)):
                    element = self.test_three[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.test_three[i] = element.to_alipay_dict()
            if hasattr(self.test_three, 'to_alipay_dict'):
                params['test_three'] = self.test_three.to_alipay_dict()
            else:
                params['test_three'] = self.test_three
        if self.test_two:
            if hasattr(self.test_two, 'to_alipay_dict'):
                params['test_two'] = self.test_two.to_alipay_dict()
            else:
                params['test_two'] = self.test_two
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskHahaIsptestQueryModel()
        if 'test_five' in d:
            o.test_five = d['test_five']
        if 'test_four' in d:
            o.test_four = d['test_four']
        if 'test_one' in d:
            o.test_one = d['test_one']
        if 'test_three' in d:
            o.test_three = d['test_three']
        if 'test_two' in d:
            o.test_two = d['test_two']
        return o


