#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApmobileAppParam import ApmobileAppParam


class AlipayDigitalmgmtAppDetecttaskCreateModel(object):

    def __init__(self):
        self._app_param = None
        self._client_id = None
        self._product_code = None
        self._source = None
        self._trace_id = None

    @property
    def app_param(self):
        return self._app_param

    @app_param.setter
    def app_param(self, value):
        if isinstance(value, ApmobileAppParam):
            self._app_param = value
        else:
            self._app_param = ApmobileAppParam.from_alipay_dict(value)
    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, value):
        self._client_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_param:
            if hasattr(self.app_param, 'to_alipay_dict'):
                params['app_param'] = self.app_param.to_alipay_dict()
            else:
                params['app_param'] = self.app_param
        if self.client_id:
            if hasattr(self.client_id, 'to_alipay_dict'):
                params['client_id'] = self.client_id.to_alipay_dict()
            else:
                params['client_id'] = self.client_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.trace_id:
            if hasattr(self.trace_id, 'to_alipay_dict'):
                params['trace_id'] = self.trace_id.to_alipay_dict()
            else:
                params['trace_id'] = self.trace_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtAppDetecttaskCreateModel()
        if 'app_param' in d:
            o.app_param = d['app_param']
        if 'client_id' in d:
            o.client_id = d['client_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'source' in d:
            o.source = d['source']
        if 'trace_id' in d:
            o.trace_id = d['trace_id']
        return o


