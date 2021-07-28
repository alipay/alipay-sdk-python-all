#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Result(object):

    def __init__(self):
        self._result_code = None
        self._result_message = None
        self._result_status = None

    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_message(self):
        return self._result_message

    @result_message.setter
    def result_message(self, value):
        self._result_message = value
    @property
    def result_status(self):
        return self._result_status

    @result_status.setter
    def result_status(self, value):
        self._result_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.result_code:
            if hasattr(self.result_code, 'to_alipay_dict'):
                params['result_code'] = self.result_code.to_alipay_dict()
            else:
                params['result_code'] = self.result_code
        if self.result_message:
            if hasattr(self.result_message, 'to_alipay_dict'):
                params['result_message'] = self.result_message.to_alipay_dict()
            else:
                params['result_message'] = self.result_message
        if self.result_status:
            if hasattr(self.result_status, 'to_alipay_dict'):
                params['result_status'] = self.result_status.to_alipay_dict()
            else:
                params['result_status'] = self.result_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Result()
        if 'result_code' in d:
            o.result_code = d['result_code']
        if 'result_message' in d:
            o.result_message = d['result_message']
        if 'result_status' in d:
            o.result_status = d['result_status']
        return o


