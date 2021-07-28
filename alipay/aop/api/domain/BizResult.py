#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BizResult(object):

    def __init__(self):
        self._encoded_result_obj = None
        self._error_code = None
        self._error_msg = None
        self._error_view_msg = None
        self._need_retry = None
        self._success = None

    @property
    def encoded_result_obj(self):
        return self._encoded_result_obj

    @encoded_result_obj.setter
    def encoded_result_obj(self, value):
        self._encoded_result_obj = value
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
    def error_view_msg(self):
        return self._error_view_msg

    @error_view_msg.setter
    def error_view_msg(self, value):
        self._error_view_msg = value
    @property
    def need_retry(self):
        return self._need_retry

    @need_retry.setter
    def need_retry(self, value):
        self._need_retry = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value


    def to_alipay_dict(self):
        params = dict()
        if self.encoded_result_obj:
            if hasattr(self.encoded_result_obj, 'to_alipay_dict'):
                params['encoded_result_obj'] = self.encoded_result_obj.to_alipay_dict()
            else:
                params['encoded_result_obj'] = self.encoded_result_obj
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
        if self.error_view_msg:
            if hasattr(self.error_view_msg, 'to_alipay_dict'):
                params['error_view_msg'] = self.error_view_msg.to_alipay_dict()
            else:
                params['error_view_msg'] = self.error_view_msg
        if self.need_retry:
            if hasattr(self.need_retry, 'to_alipay_dict'):
                params['need_retry'] = self.need_retry.to_alipay_dict()
            else:
                params['need_retry'] = self.need_retry
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
        o = BizResult()
        if 'encoded_result_obj' in d:
            o.encoded_result_obj = d['encoded_result_obj']
        if 'error_code' in d:
            o.error_code = d['error_code']
        if 'error_msg' in d:
            o.error_msg = d['error_msg']
        if 'error_view_msg' in d:
            o.error_view_msg = d['error_view_msg']
        if 'need_retry' in d:
            o.need_retry = d['need_retry']
        if 'success' in d:
            o.success = d['success']
        return o


