#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HomeApiResponse(object):

    def __init__(self):
        self._request_id = None
        self._result_code = None
        self._result_json = None
        self._result_msg = None
        self._success = None

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
    def result_json(self):
        return self._result_json

    @result_json.setter
    def result_json(self, value):
        self._result_json = value
    @property
    def result_msg(self):
        return self._result_msg

    @result_msg.setter
    def result_msg(self, value):
        self._result_msg = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value


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
        if self.result_json:
            if hasattr(self.result_json, 'to_alipay_dict'):
                params['result_json'] = self.result_json.to_alipay_dict()
            else:
                params['result_json'] = self.result_json
        if self.result_msg:
            if hasattr(self.result_msg, 'to_alipay_dict'):
                params['result_msg'] = self.result_msg.to_alipay_dict()
            else:
                params['result_msg'] = self.result_msg
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
        o = HomeApiResponse()
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'result_code' in d:
            o.result_code = d['result_code']
        if 'result_json' in d:
            o.result_json = d['result_json']
        if 'result_msg' in d:
            o.result_msg = d['result_msg']
        if 'success' in d:
            o.success = d['success']
        return o


