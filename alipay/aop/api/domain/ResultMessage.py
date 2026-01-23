#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ResultMessage(object):

    def __init__(self):
        self._error_code = None
        self._error_message = None
        self._result_flag = None

    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        self._error_message = value
    @property
    def result_flag(self):
        return self._result_flag

    @result_flag.setter
    def result_flag(self, value):
        self._result_flag = value


    def to_alipay_dict(self):
        params = dict()
        if self.error_code:
            if hasattr(self.error_code, 'to_alipay_dict'):
                params['error_code'] = self.error_code.to_alipay_dict()
            else:
                params['error_code'] = self.error_code
        if self.error_message:
            if hasattr(self.error_message, 'to_alipay_dict'):
                params['error_message'] = self.error_message.to_alipay_dict()
            else:
                params['error_message'] = self.error_message
        if self.result_flag:
            if hasattr(self.result_flag, 'to_alipay_dict'):
                params['result_flag'] = self.result_flag.to_alipay_dict()
            else:
                params['result_flag'] = self.result_flag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ResultMessage()
        if 'error_code' in d:
            o.error_code = d['error_code']
        if 'error_message' in d:
            o.error_message = d['error_message']
        if 'result_flag' in d:
            o.result_flag = d['result_flag']
        return o


