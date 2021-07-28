#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLogisticsInvoiceIstdwaybillQueryModel(object):

    def __init__(self):
        self._logistics_code = None
        self._out_invoice_request_no = None

    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def out_invoice_request_no(self):
        return self._out_invoice_request_no

    @out_invoice_request_no.setter
    def out_invoice_request_no(self, value):
        self._out_invoice_request_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        if self.out_invoice_request_no:
            if hasattr(self.out_invoice_request_no, 'to_alipay_dict'):
                params['out_invoice_request_no'] = self.out_invoice_request_no.to_alipay_dict()
            else:
                params['out_invoice_request_no'] = self.out_invoice_request_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsInvoiceIstdwaybillQueryModel()
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'out_invoice_request_no' in d:
            o.out_invoice_request_no = d['out_invoice_request_no']
        return o


