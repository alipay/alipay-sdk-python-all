#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DataInputParam import DataInputParam


class AlipaySecurityDataRiskservicecloudInputSendModel(object):

    def __init__(self):
        self._input_code = None
        self._params = None
        self._request_id = None

    @property
    def input_code(self):
        return self._input_code

    @input_code.setter
    def input_code(self, value):
        self._input_code = value
    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        if isinstance(value, list):
            self._params = list()
            for i in value:
                if isinstance(i, DataInputParam):
                    self._params.append(i)
                else:
                    self._params.append(DataInputParam.from_alipay_dict(i))
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.input_code:
            if hasattr(self.input_code, 'to_alipay_dict'):
                params['input_code'] = self.input_code.to_alipay_dict()
            else:
                params['input_code'] = self.input_code
        if self.params:
            if isinstance(self.params, list):
                for i in range(0, len(self.params)):
                    element = self.params[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.params[i] = element.to_alipay_dict()
            if hasattr(self.params, 'to_alipay_dict'):
                params['params'] = self.params.to_alipay_dict()
            else:
                params['params'] = self.params
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityDataRiskservicecloudInputSendModel()
        if 'input_code' in d:
            o.input_code = d['input_code']
        if 'params' in d:
            o.params = d['params']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


