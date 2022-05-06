#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HahaIspTestDO(object):

    def __init__(self):
        self._one = None
        self._two = None

    @property
    def one(self):
        return self._one

    @one.setter
    def one(self, value):
        self._one = value
    @property
    def two(self):
        return self._two

    @two.setter
    def two(self, value):
        self._two = value


    def to_alipay_dict(self):
        params = dict()
        if self.one:
            if hasattr(self.one, 'to_alipay_dict'):
                params['one'] = self.one.to_alipay_dict()
            else:
                params['one'] = self.one
        if self.two:
            if hasattr(self.two, 'to_alipay_dict'):
                params['two'] = self.two.to_alipay_dict()
            else:
                params['two'] = self.two
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HahaIspTestDO()
        if 'one' in d:
            o.one = d['one']
        if 'two' in d:
            o.two = d['two']
        return o


