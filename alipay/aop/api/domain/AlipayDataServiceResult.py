#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataServiceResult(object):

    def __init__(self):
        self._code = None
        self._message = None
        self._result = None
        self._success = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.message:
            if hasattr(self.message, 'to_alipay_dict'):
                params['message'] = self.message.to_alipay_dict()
            else:
                params['message'] = self.message
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
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
        o = AlipayDataServiceResult()
        if 'code' in d:
            o.code = d['code']
        if 'message' in d:
            o.message = d['message']
        if 'result' in d:
            o.result = d['result']
        if 'success' in d:
            o.success = d['success']
        return o


