#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEngineeringInfrastructureAllBatchqueryModel(object):

    def __init__(self):
        self._app_name = None
        self._begin = None
        self._end = None
        self._key_code = None
        self._limit = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def begin(self):
        return self._begin

    @begin.setter
    def begin(self, value):
        self._begin = value
    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        self._end = value
    @property
    def key_code(self):
        return self._key_code

    @key_code.setter
    def key_code(self, value):
        self._key_code = value
    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, value):
        self._limit = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.begin:
            if hasattr(self.begin, 'to_alipay_dict'):
                params['begin'] = self.begin.to_alipay_dict()
            else:
                params['begin'] = self.begin
        if self.end:
            if hasattr(self.end, 'to_alipay_dict'):
                params['end'] = self.end.to_alipay_dict()
            else:
                params['end'] = self.end
        if self.key_code:
            if hasattr(self.key_code, 'to_alipay_dict'):
                params['key_code'] = self.key_code.to_alipay_dict()
            else:
                params['key_code'] = self.key_code
        if self.limit:
            if hasattr(self.limit, 'to_alipay_dict'):
                params['limit'] = self.limit.to_alipay_dict()
            else:
                params['limit'] = self.limit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEngineeringInfrastructureAllBatchqueryModel()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'begin' in d:
            o.begin = d['begin']
        if 'end' in d:
            o.end = d['end']
        if 'key_code' in d:
            o.key_code = d['key_code']
        if 'limit' in d:
            o.limit = d['limit']
        return o


