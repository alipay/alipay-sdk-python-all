#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InputInvoiceCertifyOpenApiDTO(object):

    def __init__(self):
        self._invoice_ids = None
        self._operator = None
        self._platform_code = None
        self._request_no = None

    @property
    def invoice_ids(self):
        return self._invoice_ids

    @invoice_ids.setter
    def invoice_ids(self, value):
        if isinstance(value, list):
            self._invoice_ids = list()
            for i in value:
                self._invoice_ids.append(i)
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.invoice_ids:
            if isinstance(self.invoice_ids, list):
                for i in range(0, len(self.invoice_ids)):
                    element = self.invoice_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_ids[i] = element.to_alipay_dict()
            if hasattr(self.invoice_ids, 'to_alipay_dict'):
                params['invoice_ids'] = self.invoice_ids.to_alipay_dict()
            else:
                params['invoice_ids'] = self.invoice_ids
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.request_no:
            if hasattr(self.request_no, 'to_alipay_dict'):
                params['request_no'] = self.request_no.to_alipay_dict()
            else:
                params['request_no'] = self.request_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InputInvoiceCertifyOpenApiDTO()
        if 'invoice_ids' in d:
            o.invoice_ids = d['invoice_ids']
        if 'operator' in d:
            o.operator = d['operator']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'request_no' in d:
            o.request_no = d['request_no']
        return o


