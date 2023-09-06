#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BatchResultDTO import BatchResultDTO


class BatchModifyResponse(object):

    def __init__(self):
        self._data = None
        self._response_code = None
        self._response_msg = None
        self._succeeded = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, BatchResultDTO):
            self._data = value
        else:
            self._data = BatchResultDTO.from_alipay_dict(value)
    @property
    def response_code(self):
        return self._response_code

    @response_code.setter
    def response_code(self, value):
        self._response_code = value
    @property
    def response_msg(self):
        return self._response_msg

    @response_msg.setter
    def response_msg(self, value):
        self._response_msg = value
    @property
    def succeeded(self):
        return self._succeeded

    @succeeded.setter
    def succeeded(self, value):
        self._succeeded = value


    def to_alipay_dict(self):
        params = dict()
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.response_code:
            if hasattr(self.response_code, 'to_alipay_dict'):
                params['response_code'] = self.response_code.to_alipay_dict()
            else:
                params['response_code'] = self.response_code
        if self.response_msg:
            if hasattr(self.response_msg, 'to_alipay_dict'):
                params['response_msg'] = self.response_msg.to_alipay_dict()
            else:
                params['response_msg'] = self.response_msg
        if self.succeeded:
            if hasattr(self.succeeded, 'to_alipay_dict'):
                params['succeeded'] = self.succeeded.to_alipay_dict()
            else:
                params['succeeded'] = self.succeeded
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BatchModifyResponse()
        if 'data' in d:
            o.data = d['data']
        if 'response_code' in d:
            o.response_code = d['response_code']
        if 'response_msg' in d:
            o.response_msg = d['response_msg']
        if 'succeeded' in d:
            o.succeeded = d['succeeded']
        return o


