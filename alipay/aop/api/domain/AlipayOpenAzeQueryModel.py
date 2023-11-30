#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAzeQueryModel(object):

    def __init__(self):
        self._arg_name = None
        self._open_test = None

    @property
    def arg_name(self):
        return self._arg_name

    @arg_name.setter
    def arg_name(self, value):
        self._arg_name = value
    @property
    def open_test(self):
        return self._open_test

    @open_test.setter
    def open_test(self, value):
        self._open_test = value


    def to_alipay_dict(self):
        params = dict()
        if self.arg_name:
            if hasattr(self.arg_name, 'to_alipay_dict'):
                params['arg_name'] = self.arg_name.to_alipay_dict()
            else:
                params['arg_name'] = self.arg_name
        if self.open_test:
            if hasattr(self.open_test, 'to_alipay_dict'):
                params['open_test'] = self.open_test.to_alipay_dict()
            else:
                params['open_test'] = self.open_test
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAzeQueryModel()
        if 'arg_name' in d:
            o.arg_name = d['arg_name']
        if 'open_test' in d:
            o.open_test = d['open_test']
        return o


