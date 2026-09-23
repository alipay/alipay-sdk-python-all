#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOperationServiceDigitalshopBatchqueryModel(object):

    def __init__(self):
        self._query_type = None
        self._request_data = None
        self._service_code = None

    @property
    def query_type(self):
        return self._query_type

    @query_type.setter
    def query_type(self, value):
        self._query_type = value
    @property
    def request_data(self):
        return self._request_data

    @request_data.setter
    def request_data(self, value):
        self._request_data = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.query_type:
            if hasattr(self.query_type, 'to_alipay_dict'):
                params['query_type'] = self.query_type.to_alipay_dict()
            else:
                params['query_type'] = self.query_type
        if self.request_data:
            if hasattr(self.request_data, 'to_alipay_dict'):
                params['request_data'] = self.request_data.to_alipay_dict()
            else:
                params['request_data'] = self.request_data
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationServiceDigitalshopBatchqueryModel()
        if 'query_type' in d:
            o.query_type = d['query_type']
        if 'request_data' in d:
            o.request_data = d['request_data']
        if 'service_code' in d:
            o.service_code = d['service_code']
        return o


