#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechAiCvUaAsyncQueryModel(object):

    def __init__(self):
        self._m_app_id = None
        self._service_code = None
        self._task_id = None
        self._uri = None

    @property
    def m_app_id(self):
        return self._m_app_id

    @m_app_id.setter
    def m_app_id(self, value):
        self._m_app_id = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
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
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
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
        o = AnttechAiCvUaAsyncQueryModel()
        if 'm_app_id' in d:
            o.m_app_id = d['m_app_id']
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'uri' in d:
            o.uri = d['uri']
        return o


