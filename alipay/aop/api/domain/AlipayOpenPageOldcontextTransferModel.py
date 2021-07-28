#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenPageOldcontextTransferModel(object):

    def __init__(self):
        self._param_one = None
        self._param_three = None
        self._param_two = None

    @property
    def param_one(self):
        return self._param_one

    @param_one.setter
    def param_one(self, value):
        self._param_one = value
    @property
    def param_three(self):
        return self._param_three

    @param_three.setter
    def param_three(self, value):
        self._param_three = value
    @property
    def param_two(self):
        return self._param_two

    @param_two.setter
    def param_two(self, value):
        self._param_two = value


    def to_alipay_dict(self):
        params = dict()
        if self.param_one:
            if hasattr(self.param_one, 'to_alipay_dict'):
                params['param_one'] = self.param_one.to_alipay_dict()
            else:
                params['param_one'] = self.param_one
        if self.param_three:
            if hasattr(self.param_three, 'to_alipay_dict'):
                params['param_three'] = self.param_three.to_alipay_dict()
            else:
                params['param_three'] = self.param_three
        if self.param_two:
            if hasattr(self.param_two, 'to_alipay_dict'):
                params['param_two'] = self.param_two.to_alipay_dict()
            else:
                params['param_two'] = self.param_two
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPageOldcontextTransferModel()
        if 'param_one' in d:
            o.param_one = d['param_one']
        if 'param_three' in d:
            o.param_three = d['param_three']
        if 'param_two' in d:
            o.param_two = d['param_two']
        return o


