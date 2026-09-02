#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReverseResultList(object):

    def __init__(self):
        self._data_id = None
        self._is_success = None
        self._result_code = None

    @property
    def data_id(self):
        return self._data_id

    @data_id.setter
    def data_id(self, value):
        self._data_id = value
    @property
    def is_success(self):
        return self._is_success

    @is_success.setter
    def is_success(self, value):
        self._is_success = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_id:
            if hasattr(self.data_id, 'to_alipay_dict'):
                params['data_id'] = self.data_id.to_alipay_dict()
            else:
                params['data_id'] = self.data_id
        if self.is_success:
            if hasattr(self.is_success, 'to_alipay_dict'):
                params['is_success'] = self.is_success.to_alipay_dict()
            else:
                params['is_success'] = self.is_success
        if self.result_code:
            if hasattr(self.result_code, 'to_alipay_dict'):
                params['result_code'] = self.result_code.to_alipay_dict()
            else:
                params['result_code'] = self.result_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReverseResultList()
        if 'data_id' in d:
            o.data_id = d['data_id']
        if 'is_success' in d:
            o.is_success = d['is_success']
        if 'result_code' in d:
            o.result_code = d['result_code']
        return o


