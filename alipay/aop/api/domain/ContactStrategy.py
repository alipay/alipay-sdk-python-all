#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContactStrategy(object):

    def __init__(self):
        self._expect_call_time = None
        self._latest_call_time = None
        self._param_type = None

    @property
    def expect_call_time(self):
        return self._expect_call_time

    @expect_call_time.setter
    def expect_call_time(self, value):
        self._expect_call_time = value
    @property
    def latest_call_time(self):
        return self._latest_call_time

    @latest_call_time.setter
    def latest_call_time(self, value):
        self._latest_call_time = value
    @property
    def param_type(self):
        return self._param_type

    @param_type.setter
    def param_type(self, value):
        self._param_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.expect_call_time:
            if hasattr(self.expect_call_time, 'to_alipay_dict'):
                params['expect_call_time'] = self.expect_call_time.to_alipay_dict()
            else:
                params['expect_call_time'] = self.expect_call_time
        if self.latest_call_time:
            if hasattr(self.latest_call_time, 'to_alipay_dict'):
                params['latest_call_time'] = self.latest_call_time.to_alipay_dict()
            else:
                params['latest_call_time'] = self.latest_call_time
        if self.param_type:
            if hasattr(self.param_type, 'to_alipay_dict'):
                params['param_type'] = self.param_type.to_alipay_dict()
            else:
                params['param_type'] = self.param_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContactStrategy()
        if 'expect_call_time' in d:
            o.expect_call_time = d['expect_call_time']
        if 'latest_call_time' in d:
            o.latest_call_time = d['latest_call_time']
        if 'param_type' in d:
            o.param_type = d['param_type']
        return o


