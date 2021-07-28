#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ClearingCommonResult(object):

    def __init__(self):
        self._result_code = None
        self._result_description = None
        self._success = None

    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_description(self):
        return self._result_description

    @result_description.setter
    def result_description(self, value):
        self._result_description = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value


    def to_alipay_dict(self):
        params = dict()
        if self.result_code:
            if hasattr(self.result_code, 'to_alipay_dict'):
                params['result_code'] = self.result_code.to_alipay_dict()
            else:
                params['result_code'] = self.result_code
        if self.result_description:
            if hasattr(self.result_description, 'to_alipay_dict'):
                params['result_description'] = self.result_description.to_alipay_dict()
            else:
                params['result_description'] = self.result_description
        if self.success:
            if hasattr(self.success, 'to_alipay_dict'):
                params['success'] = self.success.to_alipay_dict()
            else:
                params['success'] = self.success
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ClearingCommonResult()
        if 'result_code' in d:
            o.result_code = d['result_code']
        if 'result_description' in d:
            o.result_description = d['result_description']
        if 'success' in d:
            o.success = d['success']
        return o


