#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechAiCvUaAsyncIdentifyModel(object):

    def __init__(self):
        self._m_app_id = None
        self._params = None
        self._service_code = None
        self._trace_id = None
        self._uri = None

    @property
    def m_app_id(self):
        return self._m_app_id

    @m_app_id.setter
    def m_app_id(self, value):
        self._m_app_id = value
    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value
    @property
    def uri(self):
        return self._uri

    @uri.setter
    def uri(self, value):
        self._uri = value


    def to_alipay_dict(self):
        params = dict()
        if self.m_app_id:
            if hasattr(self.m_app_id, 'to_alipay_dict'):
                params['m_app_id'] = self.m_app_id.to_alipay_dict()
            else:
                params['m_app_id'] = self.m_app_id
        if self.params:
            if hasattr(self.params, 'to_alipay_dict'):
                params['params'] = self.params.to_alipay_dict()
            else:
                params['params'] = self.params
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        if self.trace_id:
            if hasattr(self.trace_id, 'to_alipay_dict'):
                params['trace_id'] = self.trace_id.to_alipay_dict()
            else:
                params['trace_id'] = self.trace_id
        if self.uri:
            if hasattr(self.uri, 'to_alipay_dict'):
                params['uri'] = self.uri.to_alipay_dict()
            else:
                params['uri'] = self.uri
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechAiCvUaAsyncIdentifyModel()
        if 'm_app_id' in d:
            o.m_app_id = d['m_app_id']
        if 'params' in d:
            o.params = d['params']
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'trace_id' in d:
            o.trace_id = d['trace_id']
        if 'uri' in d:
            o.uri = d['uri']
        return o


