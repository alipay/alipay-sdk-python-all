#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ProductInvoiceCheckResult(object):

    def __init__(self):
        self._check_code = None
        self._check_time = None
        self._code = None
        self._message = None

    @property
    def check_code(self):
        return self._check_code

    @check_code.setter
    def check_code(self, value):
        self._check_code = value
    @property
    def check_time(self):
        return self._check_time

    @check_time.setter
    def check_time(self, value):
        self._check_time = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.check_code:
            if hasattr(self.check_code, 'to_alipay_dict'):
                params['check_code'] = self.check_code.to_alipay_dict()
            else:
                params['check_code'] = self.check_code
        if self.check_time:
            if hasattr(self.check_time, 'to_alipay_dict'):
                params['check_time'] = self.check_time.to_alipay_dict()
            else:
                params['check_time'] = self.check_time
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProductInvoiceCheckResult()
        if 'check_code' in d:
            o.check_code = d['check_code']
        if 'check_time' in d:
            o.check_time = d['check_time']
        if 'code' in d:
            o.code = d['code']
        if 'message' in d:
            o.message = d['message']
        return o


