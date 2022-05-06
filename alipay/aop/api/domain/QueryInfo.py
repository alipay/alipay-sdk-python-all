#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QueryInfo(object):

    def __init__(self):
        self._app_name = None
        self._operator = None
        self._query_type = None
        self._user_no = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def query_type(self):
        return self._query_type

    @query_type.setter
    def query_type(self, value):
        self._query_type = value
    @property
    def user_no(self):
        return self._user_no

    @user_no.setter
    def user_no(self, value):
        self._user_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.query_type:
            if hasattr(self.query_type, 'to_alipay_dict'):
                params['query_type'] = self.query_type.to_alipay_dict()
            else:
                params['query_type'] = self.query_type
        if self.user_no:
            if hasattr(self.user_no, 'to_alipay_dict'):
                params['user_no'] = self.user_no.to_alipay_dict()
            else:
                params['user_no'] = self.user_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QueryInfo()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'operator' in d:
            o.operator = d['operator']
        if 'query_type' in d:
            o.query_type = d['query_type']
        if 'user_no' in d:
            o.user_no = d['user_no']
        return o


