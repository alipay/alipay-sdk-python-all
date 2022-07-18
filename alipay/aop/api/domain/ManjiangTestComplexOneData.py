#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ManjiangTestComplexOneData(object):

    def __init__(self):
        self._test_level_one = None

    @property
    def test_level_one(self):
        return self._test_level_one

    @test_level_one.setter
    def test_level_one(self, value):
        self._test_level_one = value


    def to_alipay_dict(self):
        params = dict()
        if self.test_level_one:
            if hasattr(self.test_level_one, 'to_alipay_dict'):
                params['test_level_one'] = self.test_level_one.to_alipay_dict()
            else:
                params['test_level_one'] = self.test_level_one
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ManjiangTestComplexOneData()
        if 'test_level_one' in d:
            o.test_level_one = d['test_level_one']
        return o


