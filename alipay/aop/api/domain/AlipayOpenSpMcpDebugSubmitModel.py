#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NameValueParam import NameValueParam
from alipay.aop.api.domain.NameValueParam import NameValueParam


class AlipayOpenSpMcpDebugSubmitModel(object):

    def __init__(self):
        self._ability_code = None
        self._headers = None
        self._query_params = None
        self._tool_code = None
        self._tool_schema = None

    @property
    def ability_code(self):
        return self._ability_code

    @ability_code.setter
    def ability_code(self, value):
        self._ability_code = value
    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, value):
        if isinstance(value, list):
            self._headers = list()
            for i in value:
                if isinstance(i, NameValueParam):
                    self._headers.append(i)
                else:
                    self._headers.append(NameValueParam.from_alipay_dict(i))
    @property
    def query_params(self):
        return self._query_params

    @query_params.setter
    def query_params(self, value):
        if isinstance(value, list):
            self._query_params = list()
            for i in value:
                if isinstance(i, NameValueParam):
                    self._query_params.append(i)
                else:
                    self._query_params.append(NameValueParam.from_alipay_dict(i))
    @property
    def tool_code(self):
        return self._tool_code

    @tool_code.setter
    def tool_code(self, value):
        self._tool_code = value
    @property
    def tool_schema(self):
        return self._tool_schema

    @tool_schema.setter
    def tool_schema(self, value):
        self._tool_schema = value


    def to_alipay_dict(self):
        params = dict()
        if self.ability_code:
            if hasattr(self.ability_code, 'to_alipay_dict'):
                params['ability_code'] = self.ability_code.to_alipay_dict()
            else:
                params['ability_code'] = self.ability_code
        if self.headers:
            if isinstance(self.headers, list):
                for i in range(0, len(self.headers)):
                    element = self.headers[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.headers[i] = element.to_alipay_dict()
            if hasattr(self.headers, 'to_alipay_dict'):
                params['headers'] = self.headers.to_alipay_dict()
            else:
                params['headers'] = self.headers
        if self.query_params:
            if isinstance(self.query_params, list):
                for i in range(0, len(self.query_params)):
                    element = self.query_params[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.query_params[i] = element.to_alipay_dict()
            if hasattr(self.query_params, 'to_alipay_dict'):
                params['query_params'] = self.query_params.to_alipay_dict()
            else:
                params['query_params'] = self.query_params
        if self.tool_code:
            if hasattr(self.tool_code, 'to_alipay_dict'):
                params['tool_code'] = self.tool_code.to_alipay_dict()
            else:
                params['tool_code'] = self.tool_code
        if self.tool_schema:
            if hasattr(self.tool_schema, 'to_alipay_dict'):
                params['tool_schema'] = self.tool_schema.to_alipay_dict()
            else:
                params['tool_schema'] = self.tool_schema
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpMcpDebugSubmitModel()
        if 'ability_code' in d:
            o.ability_code = d['ability_code']
        if 'headers' in d:
            o.headers = d['headers']
        if 'query_params' in d:
            o.query_params = d['query_params']
        if 'tool_code' in d:
            o.tool_code = d['tool_code']
        if 'tool_schema' in d:
            o.tool_schema = d['tool_schema']
        return o


