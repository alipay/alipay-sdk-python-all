#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItapResponsePayload(object):

    def __init__(self):
        self._result = None
        self._result_code = None
        self._result_msg = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_msg(self):
        return self._result_msg

    @result_msg.setter
    def result_msg(self, value):
        self._result_msg = value


    def to_alipay_dict(self):
        params = dict()
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
        if self.result_code:
            if hasattr(self.result_code, 'to_alipay_dict'):
                params['result_code'] = self.result_code.to_alipay_dict()
            else:
                params['result_code'] = self.result_code
        if self.result_msg:
            if hasattr(self.result_msg, 'to_alipay_dict'):
                params['result_msg'] = self.result_msg.to_alipay_dict()
            else:
                params['result_msg'] = self.result_msg
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItapResponsePayload()
        if 'result' in d:
            o.result = d['result']
        if 'result_code' in d:
            o.result_code = d['result_code']
        if 'result_msg' in d:
            o.result_msg = d['result_msg']
        return o


