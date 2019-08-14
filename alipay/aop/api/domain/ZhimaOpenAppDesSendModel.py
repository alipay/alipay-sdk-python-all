#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GavintestNewLeveaOne import GavintestNewLeveaOne


class ZhimaOpenAppDesSendModel(object):

    def __init__(self):
        self._com = None
        self._test = None

    @property
    def com(self):
        return self._com

    @com.setter
    def com(self, value):
        if isinstance(value, GavintestNewLeveaOne):
            self._com = value
        else:
            self._com = GavintestNewLeveaOne.from_alipay_dict(value)
    @property
    def test(self):
        return self._test

    @test.setter
    def test(self, value):
        self._test = value


    def to_alipay_dict(self):
        params = dict()
        if self.com:
            if hasattr(self.com, 'to_alipay_dict'):
                params['com'] = self.com.to_alipay_dict()
            else:
                params['com'] = self.com
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
        o = ZhimaOpenAppDesSendModel()
        if 'com' in d:
            o.com = d['com']
        if 'test' in d:
            o.test = d['test']
        return o


