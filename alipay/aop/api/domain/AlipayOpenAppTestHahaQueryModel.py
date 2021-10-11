#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LogisticsAccountStatusDTO import LogisticsAccountStatusDTO


class AlipayOpenAppTestHahaQueryModel(object):

    def __init__(self):
        self._test_one = None
        self._test_three = None
        self._test_two = None

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
        if isinstance(value, LogisticsAccountStatusDTO):
            self._test_three = value
        else:
            self._test_three = LogisticsAccountStatusDTO.from_alipay_dict(value)
    @property
    def test_two(self):
        return self._test_two

    @test_two.setter
    def test_two(self, value):
        self._test_two = value


    def to_alipay_dict(self):
        params = dict()
        if self.test_one:
            if hasattr(self.test_one, 'to_alipay_dict'):
                params['test_one'] = self.test_one.to_alipay_dict()
            else:
                params['test_one'] = self.test_one
        if self.test_three:
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
        o = AlipayOpenAppTestHahaQueryModel()
        if 'test_one' in d:
            o.test_one = d['test_one']
        if 'test_three' in d:
            o.test_three = d['test_three']
        if 'test_two' in d:
            o.test_two = d['test_two']
        return o


