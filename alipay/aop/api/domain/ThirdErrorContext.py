#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ThirdErrorContext(object):

    def __init__(self):
        self._third_error_code = None
        self._third_error_msg = None

    @property
    def third_error_code(self):
        return self._third_error_code

    @third_error_code.setter
    def third_error_code(self, value):
        self._third_error_code = value
    @property
    def third_error_msg(self):
        return self._third_error_msg

    @third_error_msg.setter
    def third_error_msg(self, value):
        self._third_error_msg = value


    def to_alipay_dict(self):
        params = dict()
        if self.third_error_code:
            if hasattr(self.third_error_code, 'to_alipay_dict'):
                params['third_error_code'] = self.third_error_code.to_alipay_dict()
            else:
                params['third_error_code'] = self.third_error_code
        if self.third_error_msg:
            if hasattr(self.third_error_msg, 'to_alipay_dict'):
                params['third_error_msg'] = self.third_error_msg.to_alipay_dict()
            else:
                params['third_error_msg'] = self.third_error_msg
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ThirdErrorContext()
        if 'third_error_code' in d:
            o.third_error_code = d['third_error_code']
        if 'third_error_msg' in d:
            o.third_error_msg = d['third_error_msg']
        return o


