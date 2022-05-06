#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FailFaceUserInfo(object):

    def __init__(self):
        self._fail_code = None
        self._fail_message = None
        self._retry = None
        self._unique_id = None

    @property
    def fail_code(self):
        return self._fail_code

    @fail_code.setter
    def fail_code(self, value):
        self._fail_code = value
    @property
    def fail_message(self):
        return self._fail_message

    @fail_message.setter
    def fail_message(self, value):
        self._fail_message = value
    @property
    def retry(self):
        return self._retry

    @retry.setter
    def retry(self, value):
        self._retry = value
    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.fail_code:
            if hasattr(self.fail_code, 'to_alipay_dict'):
                params['fail_code'] = self.fail_code.to_alipay_dict()
            else:
                params['fail_code'] = self.fail_code
        if self.fail_message:
            if hasattr(self.fail_message, 'to_alipay_dict'):
                params['fail_message'] = self.fail_message.to_alipay_dict()
            else:
                params['fail_message'] = self.fail_message
        if self.retry:
            if hasattr(self.retry, 'to_alipay_dict'):
                params['retry'] = self.retry.to_alipay_dict()
            else:
                params['retry'] = self.retry
        if self.unique_id:
            if hasattr(self.unique_id, 'to_alipay_dict'):
                params['unique_id'] = self.unique_id.to_alipay_dict()
            else:
                params['unique_id'] = self.unique_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FailFaceUserInfo()
        if 'fail_code' in d:
            o.fail_code = d['fail_code']
        if 'fail_message' in d:
            o.fail_message = d['fail_message']
        if 'retry' in d:
            o.retry = d['retry']
        if 'unique_id' in d:
            o.unique_id = d['unique_id']
        return o


