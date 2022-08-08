#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Marketingtest import Marketingtest


class Marketingtestt(object):

    def __init__(self):
        self._test_22 = None

    @property
    def test_22(self):
        return self._test_22

    @test_22.setter
    def test_22(self, value):
        if isinstance(value, Marketingtest):
            self._test_22 = value
        else:
            self._test_22 = Marketingtest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
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
        o = Marketingtestt()
        if 'test_22' in d:
            o.test_22 = d['test_22']
        return o


