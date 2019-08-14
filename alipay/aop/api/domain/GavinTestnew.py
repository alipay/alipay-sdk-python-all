#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GavinTestnew(object):

    def __init__(self):
        self._test = None

    @property
    def test(self):
        return self._test

    @test.setter
    def test(self, value):
        self._test = value


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
        o = GavinTestnew()
        if 'test' in d:
            o.test = d['test']
        return o


