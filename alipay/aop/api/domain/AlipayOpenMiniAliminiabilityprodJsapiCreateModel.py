#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.JsApiBaseDTO import JsApiBaseDTO
from alipay.aop.api.domain.ErrorCodeDTO import ErrorCodeDTO


class AlipayOpenMiniAliminiabilityprodJsapiCreateModel(object):

    def __init__(self):
        self._api_base_request = None
        self._api_error_code_request = None
        self._in_param_requests = None
        self._out_param_requests = None

    @property
    def api_base_request(self):
        return self._api_base_request

    @api_base_request.setter
    def api_base_request(self, value):
        if isinstance(value, JsApiBaseDTO):
            self._api_base_request = value
        else:
            self._api_base_request = JsApiBaseDTO.from_alipay_dict(value)
    @property
    def api_error_code_request(self):
        return self._api_error_code_request

    @api_error_code_request.setter
    def api_error_code_request(self, value):
        if isinstance(value, list):
            self._api_error_code_request = list()
            for i in value:
                if isinstance(i, ErrorCodeDTO):
                    self._api_error_code_request.append(i)
                else:
                    self._api_error_code_request.append(ErrorCodeDTO.from_alipay_dict(i))
    @property
    def in_param_requests(self):
        return self._in_param_requests

    @in_param_requests.setter
    def in_param_requests(self, value):
        self._in_param_requests = value
    @property
    def out_param_requests(self):
        return self._out_param_requests

    @out_param_requests.setter
    def out_param_requests(self, value):
        self._out_param_requests = value


    def to_alipay_dict(self):
        params = dict()
        if self.api_base_request:
            if hasattr(self.api_base_request, 'to_alipay_dict'):
                params['api_base_request'] = self.api_base_request.to_alipay_dict()
            else:
                params['api_base_request'] = self.api_base_request
        if self.api_error_code_request:
            if isinstance(self.api_error_code_request, list):
                for i in range(0, len(self.api_error_code_request)):
                    element = self.api_error_code_request[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.api_error_code_request[i] = element.to_alipay_dict()
            if hasattr(self.api_error_code_request, 'to_alipay_dict'):
                params['api_error_code_request'] = self.api_error_code_request.to_alipay_dict()
            else:
                params['api_error_code_request'] = self.api_error_code_request
        if self.in_param_requests:
            if hasattr(self.in_param_requests, 'to_alipay_dict'):
                params['in_param_requests'] = self.in_param_requests.to_alipay_dict()
            else:
                params['in_param_requests'] = self.in_param_requests
        if self.out_param_requests:
            if hasattr(self.out_param_requests, 'to_alipay_dict'):
                params['out_param_requests'] = self.out_param_requests.to_alipay_dict()
            else:
                params['out_param_requests'] = self.out_param_requests
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniAliminiabilityprodJsapiCreateModel()
        if 'api_base_request' in d:
            o.api_base_request = d['api_base_request']
        if 'api_error_code_request' in d:
            o.api_error_code_request = d['api_error_code_request']
        if 'in_param_requests' in d:
            o.in_param_requests = d['in_param_requests']
        if 'out_param_requests' in d:
            o.out_param_requests = d['out_param_requests']
        return o


