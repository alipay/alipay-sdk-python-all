#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExceptionInfo(object):

    def __init__(self):
        self._exp_code = None
        self._exp_time = None

    @property
    def exp_code(self):
        return self._exp_code

    @exp_code.setter
    def exp_code(self, value):
        self._exp_code = value
    @property
    def exp_time(self):
        return self._exp_time

    @exp_time.setter
    def exp_time(self, value):
        self._exp_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.exp_code:
            if hasattr(self.exp_code, 'to_alipay_dict'):
                params['exp_code'] = self.exp_code.to_alipay_dict()
            else:
                params['exp_code'] = self.exp_code
        if self.exp_time:
            if hasattr(self.exp_time, 'to_alipay_dict'):
                params['exp_time'] = self.exp_time.to_alipay_dict()
            else:
                params['exp_time'] = self.exp_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExceptionInfo()
        if 'exp_code' in d:
            o.exp_code = d['exp_code']
        if 'exp_time' in d:
            o.exp_time = d['exp_time']
        return o


