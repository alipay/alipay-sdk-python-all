#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Marketingtest(object):

    def __init__(self):
        self._test_21 = None

    @property
    def test_21(self):
        return self._test_21

    @test_21.setter
    def test_21(self, value):
        self._test_21 = value


    def to_alipay_dict(self):
        params = dict()
        if self.test_21:
            if hasattr(self.test_21, 'to_alipay_dict'):
                params['test_21'] = self.test_21.to_alipay_dict()
            else:
                params['test_21'] = self.test_21
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Marketingtest()
        if 'test_21' in d:
            o.test_21 = d['test_21']
        return o


