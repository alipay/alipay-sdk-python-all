#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ManjiangTestComplexOneData(object):

    def __init__(self):
        self._sss = None
        self._ssssd = None
        self._test_level_one = None

    @property
    def sss(self):
        return self._sss

    @sss.setter
    def sss(self, value):
        self._sss = value
    @property
    def ssssd(self):
        return self._ssssd

    @ssssd.setter
    def ssssd(self, value):
        self._ssssd = value
    @property
    def test_level_one(self):
        return self._test_level_one

    @test_level_one.setter
    def test_level_one(self, value):
        self._test_level_one = value


    def to_alipay_dict(self):
        params = dict()
        if self.sss:
            if hasattr(self.sss, 'to_alipay_dict'):
                params['sss'] = self.sss.to_alipay_dict()
            else:
                params['sss'] = self.sss
        if self.ssssd:
            if hasattr(self.ssssd, 'to_alipay_dict'):
                params['ssssd'] = self.ssssd.to_alipay_dict()
            else:
                params['ssssd'] = self.ssssd
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
        if 'sss' in d:
            o.sss = d['sss']
        if 'ssssd' in d:
            o.ssssd = d['ssssd']
        if 'test_level_one' in d:
            o.test_level_one = d['test_level_one']
        return o


