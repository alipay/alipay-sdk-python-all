#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ResultModelForInvoiceBill(object):

    def __init__(self):
        self._error_code = None
        self._error_detail_info = None
        self._error_msg = None
        self._success = None

    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_detail_info(self):
        return self._error_detail_info

    @error_detail_info.setter
    def error_detail_info(self, value):
        self._error_detail_info = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value


    def to_alipay_dict(self):
        params = dict()
        if self.error_code:
            if hasattr(self.error_code, 'to_alipay_dict'):
                params['error_code'] = self.error_code.to_alipay_dict()
            else:
                params['error_code'] = self.error_code
        if self.error_detail_info:
            if hasattr(self.error_detail_info, 'to_alipay_dict'):
                params['error_detail_info'] = self.error_detail_info.to_alipay_dict()
            else:
                params['error_detail_info'] = self.error_detail_info
        if self.error_msg:
            if hasattr(self.error_msg, 'to_alipay_dict'):
                params['error_msg'] = self.error_msg.to_alipay_dict()
            else:
                params['error_msg'] = self.error_msg
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
        o = ResultModelForInvoiceBill()
        if 'error_code' in d:
            o.error_code = d['error_code']
        if 'error_detail_info' in d:
            o.error_detail_info = d['error_detail_info']
        if 'error_msg' in d:
            o.error_msg = d['error_msg']
        if 'success' in d:
            o.success = d['success']
        return o


