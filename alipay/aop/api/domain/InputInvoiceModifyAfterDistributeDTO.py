#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InputInvoiceModifyOpenApiDTO import InputInvoiceModifyOpenApiDTO


class InputInvoiceModifyAfterDistributeDTO(object):

    def __init__(self):
        self._input_invoice_modify_open_api_dto = None
        self._operator = None
        self._platform_code = None
        self._request_no = None

    @property
    def input_invoice_modify_open_api_dto(self):
        return self._input_invoice_modify_open_api_dto

    @input_invoice_modify_open_api_dto.setter
    def input_invoice_modify_open_api_dto(self, value):
        if isinstance(value, InputInvoiceModifyOpenApiDTO):
            self._input_invoice_modify_open_api_dto = value
        else:
            self._input_invoice_modify_open_api_dto = InputInvoiceModifyOpenApiDTO.from_alipay_dict(value)
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
        if self.input_invoice_modify_open_api_dto:
            if hasattr(self.input_invoice_modify_open_api_dto, 'to_alipay_dict'):
                params['input_invoice_modify_open_api_dto'] = self.input_invoice_modify_open_api_dto.to_alipay_dict()
            else:
                params['input_invoice_modify_open_api_dto'] = self.input_invoice_modify_open_api_dto
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
        o = InputInvoiceModifyAfterDistributeDTO()
        if 'input_invoice_modify_open_api_dto' in d:
            o.input_invoice_modify_open_api_dto = d['input_invoice_modify_open_api_dto']
        if 'operator' in d:
            o.operator = d['operator']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'request_no' in d:
            o.request_no = d['request_no']
        return o


