#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TestHq import TestHq


class AlipayDataHqteessQueryModel(object):

    def __init__(self):
        self._test = None

    @property
    def test(self):
        return self._test

    @test.setter
    def test(self, value):
        if isinstance(value, TestHq):
            self._test = value
        else:
            self._test = TestHq.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.test:
            if hasattr(self.test, 'to_alipay_dict'):
                params['test'] = self.test.to_alipay_dict()
            else:
                params['test'] = self.test
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataHqteessQueryModel()
        if 'test' in d:
            o.test = d['test']
        return o


