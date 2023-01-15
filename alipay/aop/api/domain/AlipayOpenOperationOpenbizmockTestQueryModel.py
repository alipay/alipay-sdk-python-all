#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TestDemoWzw import TestDemoWzw


class AlipayOpenOperationOpenbizmockTestQueryModel(object):

    def __init__(self):
        self._fuza = None
        self._out_open_id = None
        self._u_test = None

    @property
    def fuza(self):
        return self._fuza

    @fuza.setter
    def fuza(self, value):
        if isinstance(value, TestDemoWzw):
            self._fuza = value
        else:
            self._fuza = TestDemoWzw.from_alipay_dict(value)
    @property
    def out_open_id(self):
        return self._out_open_id

    @out_open_id.setter
    def out_open_id(self, value):
        self._out_open_id = value
    @property
    def u_test(self):
        return self._u_test

    @u_test.setter
    def u_test(self, value):
        self._u_test = value


    def to_alipay_dict(self):
        params = dict()
        if self.fuza:
            if hasattr(self.fuza, 'to_alipay_dict'):
                params['fuza'] = self.fuza.to_alipay_dict()
            else:
                params['fuza'] = self.fuza
        if self.out_open_id:
            if hasattr(self.out_open_id, 'to_alipay_dict'):
                params['out_open_id'] = self.out_open_id.to_alipay_dict()
            else:
                params['out_open_id'] = self.out_open_id
        if self.u_test:
            if hasattr(self.u_test, 'to_alipay_dict'):
                params['u_test'] = self.u_test.to_alipay_dict()
            else:
                params['u_test'] = self.u_test
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOperationOpenbizmockTestQueryModel()
        if 'fuza' in d:
            o.fuza = d['fuza']
        if 'out_open_id' in d:
            o.out_open_id = d['out_open_id']
        if 'u_test' in d:
            o.u_test = d['u_test']
        return o


