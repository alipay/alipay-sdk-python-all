#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Marketingtest import Marketingtest
from alipay.aop.api.domain.Marketingtestt import Marketingtestt


class AlipayMarketingXuanyitestTransferModel(object):

    def __init__(self):
        self._test = None
        self._test_21 = None
        self._test_22 = None

    @property
    def test(self):
        return self._test

    @test.setter
    def test(self, value):
        if isinstance(value, list):
            self._test = list()
            for i in value:
                self._test.append(i)
    @property
    def test_21(self):
        return self._test_21

    @test_21.setter
    def test_21(self, value):
        if isinstance(value, list):
            self._test_21 = list()
            for i in value:
                if isinstance(i, Marketingtest):
                    self._test_21.append(i)
                else:
                    self._test_21.append(Marketingtest.from_alipay_dict(i))
    @property
    def test_22(self):
        return self._test_22

    @test_22.setter
    def test_22(self, value):
        if isinstance(value, Marketingtestt):
            self._test_22 = value
        else:
            self._test_22 = Marketingtestt.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.test:
            if isinstance(self.test, list):
                for i in range(0, len(self.test)):
                    element = self.test[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.test[i] = element.to_alipay_dict()
            if hasattr(self.test, 'to_alipay_dict'):
                params['test'] = self.test.to_alipay_dict()
            else:
                params['test'] = self.test
        if self.test_21:
            if isinstance(self.test_21, list):
                for i in range(0, len(self.test_21)):
                    element = self.test_21[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.test_21[i] = element.to_alipay_dict()
            if hasattr(self.test_21, 'to_alipay_dict'):
                params['test_21'] = self.test_21.to_alipay_dict()
            else:
                params['test_21'] = self.test_21
        if self.test_22:
            if hasattr(self.test_22, 'to_alipay_dict'):
                params['test_22'] = self.test_22.to_alipay_dict()
            else:
                params['test_22'] = self.test_22
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingXuanyitestTransferModel()
        if 'test' in d:
            o.test = d['test']
        if 'test_21' in d:
            o.test_21 = d['test_21']
        if 'test_22' in d:
            o.test_22 = d['test_22']
        return o


