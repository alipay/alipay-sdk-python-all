#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneQuotationQuoteinfoprodNlqueryQueryModel(object):

    def __init__(self):
        self._app_token = None
        self._file_path = None
        self._param = None
        self._query = None
        self._task_type = None

    @property
    def app_token(self):
        return self._app_token

    @app_token.setter
    def app_token(self, value):
        self._app_token = value
    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        self._file_path = value
    @property
    def param(self):
        return self._param

    @param.setter
    def param(self, value):
        self._param = value
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
    @property
    def task_type(self):
        return self._task_type

    @task_type.setter
    def task_type(self, value):
        self._task_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_token:
            if hasattr(self.app_token, 'to_alipay_dict'):
                params['app_token'] = self.app_token.to_alipay_dict()
            else:
                params['app_token'] = self.app_token
        if self.file_path:
            if hasattr(self.file_path, 'to_alipay_dict'):
                params['file_path'] = self.file_path.to_alipay_dict()
            else:
                params['file_path'] = self.file_path
        if self.param:
            if hasattr(self.param, 'to_alipay_dict'):
                params['param'] = self.param.to_alipay_dict()
            else:
                params['param'] = self.param
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        if self.task_type:
            if hasattr(self.task_type, 'to_alipay_dict'):
                params['task_type'] = self.task_type.to_alipay_dict()
            else:
                params['task_type'] = self.task_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneQuotationQuoteinfoprodNlqueryQueryModel()
        if 'app_token' in d:
            o.app_token = d['app_token']
        if 'file_path' in d:
            o.file_path = d['file_path']
        if 'param' in d:
            o.param = d['param']
        if 'query' in d:
            o.query = d['query']
        if 'task_type' in d:
            o.task_type = d['task_type']
        return o


