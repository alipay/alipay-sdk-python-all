#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeSaasInvoiceQueryModel(object):

    def __init__(self):
        self._out_request_no = None
        self._query_mode = None
        self._saas_invoice_order_no = None

    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def query_mode(self):
        return self._query_mode

    @query_mode.setter
    def query_mode(self, value):
        self._query_mode = value
    @property
    def saas_invoice_order_no(self):
        return self._saas_invoice_order_no

    @saas_invoice_order_no.setter
    def saas_invoice_order_no(self, value):
        self._saas_invoice_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.query_mode:
            if hasattr(self.query_mode, 'to_alipay_dict'):
                params['query_mode'] = self.query_mode.to_alipay_dict()
            else:
                params['query_mode'] = self.query_mode
        if self.saas_invoice_order_no:
            if hasattr(self.saas_invoice_order_no, 'to_alipay_dict'):
                params['saas_invoice_order_no'] = self.saas_invoice_order_no.to_alipay_dict()
            else:
                params['saas_invoice_order_no'] = self.saas_invoice_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeSaasInvoiceQueryModel()
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'query_mode' in d:
            o.query_mode = d['query_mode']
        if 'saas_invoice_order_no' in d:
            o.saas_invoice_order_no = d['saas_invoice_order_no']
        return o


