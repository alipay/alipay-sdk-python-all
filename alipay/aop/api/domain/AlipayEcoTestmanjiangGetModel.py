#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoTestmanjiangGetModel(object):

    def __init__(self):
        self._s = None
        self._test = None
        self._x_op = None
        self._x_sss = None
        self._x_test = None

    @property
    def s(self):
        return self._s

    @s.setter
    def s(self, value):
        self._s = value
    @property
    def test(self):
        return self._test

    @test.setter
    def test(self, value):
        self._test = value
    @property
    def x_op(self):
        return self._x_op

    @x_op.setter
    def x_op(self, value):
        self._x_op = value
    @property
    def x_sss(self):
        return self._x_sss

    @x_sss.setter
    def x_sss(self, value):
        self._x_sss = value
    @property
    def x_test(self):
        return self._x_test

    @x_test.setter
    def x_test(self, value):
        self._x_test = value


    def to_alipay_dict(self):
        params = dict()
        if self.s:
            if hasattr(self.s, 'to_alipay_dict'):
                params['s'] = self.s.to_alipay_dict()
            else:
                params['s'] = self.s
        if self.test:
            if hasattr(self.test, 'to_alipay_dict'):
                params['test'] = self.test.to_alipay_dict()
            else:
                params['test'] = self.test
        if self.x_op:
            if hasattr(self.x_op, 'to_alipay_dict'):
                params['x_op'] = self.x_op.to_alipay_dict()
            else:
                params['x_op'] = self.x_op
        if self.x_sss:
            if hasattr(self.x_sss, 'to_alipay_dict'):
                params['x_sss'] = self.x_sss.to_alipay_dict()
            else:
                params['x_sss'] = self.x_sss
        if self.x_test:
            if hasattr(self.x_test, 'to_alipay_dict'):
                params['x_test'] = self.x_test.to_alipay_dict()
            else:
                params['x_test'] = self.x_test
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoTestmanjiangGetModel()
        if 's' in d:
            o.s = d['s']
        if 'test' in d:
            o.test = d['test']
        if 'x_op' in d:
            o.x_op = d['x_op']
        if 'x_sss' in d:
            o.x_sss = d['x_sss']
        if 'x_test' in d:
            o.x_test = d['x_test']
        return o


