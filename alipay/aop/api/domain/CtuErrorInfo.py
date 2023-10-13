#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CtuErrorInfo(object):

    def __init__(self):
        self._check_result = None
        self._error_code = None
        self._error_msg = None
        self._risk_temp_code = None

    @property
    def check_result(self):
        return self._check_result

    @check_result.setter
    def check_result(self, value):
        self._check_result = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def risk_temp_code(self):
        return self._risk_temp_code

    @risk_temp_code.setter
    def risk_temp_code(self, value):
        self._risk_temp_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_result:
            if hasattr(self.check_result, 'to_alipay_dict'):
                params['check_result'] = self.check_result.to_alipay_dict()
            else:
                params['check_result'] = self.check_result
        if self.error_code:
            if hasattr(self.error_code, 'to_alipay_dict'):
                params['error_code'] = self.error_code.to_alipay_dict()
            else:
                params['error_code'] = self.error_code
        if self.error_msg:
            if hasattr(self.error_msg, 'to_alipay_dict'):
                params['error_msg'] = self.error_msg.to_alipay_dict()
            else:
                params['error_msg'] = self.error_msg
        if self.risk_temp_code:
            if hasattr(self.risk_temp_code, 'to_alipay_dict'):
                params['risk_temp_code'] = self.risk_temp_code.to_alipay_dict()
            else:
                params['risk_temp_code'] = self.risk_temp_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CtuErrorInfo()
        if 'check_result' in d:
            o.check_result = d['check_result']
        if 'error_code' in d:
            o.error_code = d['error_code']
        if 'error_msg' in d:
            o.error_msg = d['error_msg']
        if 'risk_temp_code' in d:
            o.risk_temp_code = d['risk_temp_code']
        return o


