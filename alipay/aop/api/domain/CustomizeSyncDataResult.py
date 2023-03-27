#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CustomizeSyncDataResult(object):

    def __init__(self):
        self._request_id = None
        self._result_code = None
        self._result_msg = None
        self._result_status = None
        self._sync_status = None

    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
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
    @property
    def result_status(self):
        return self._result_status

    @result_status.setter
    def result_status(self, value):
        self._result_status = value
    @property
    def sync_status(self):
        return self._sync_status

    @sync_status.setter
    def sync_status(self, value):
        self._sync_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
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
        if self.result_status:
            if hasattr(self.result_status, 'to_alipay_dict'):
                params['result_status'] = self.result_status.to_alipay_dict()
            else:
                params['result_status'] = self.result_status
        if self.sync_status:
            if hasattr(self.sync_status, 'to_alipay_dict'):
                params['sync_status'] = self.sync_status.to_alipay_dict()
            else:
                params['sync_status'] = self.sync_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CustomizeSyncDataResult()
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'result_code' in d:
            o.result_code = d['result_code']
        if 'result_msg' in d:
            o.result_msg = d['result_msg']
        if 'result_status' in d:
            o.result_status = d['result_status']
        if 'sync_status' in d:
            o.sync_status = d['sync_status']
        return o


