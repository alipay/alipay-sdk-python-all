#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeSaasInvoiceBatchqueryModel(object):

    def __init__(self):
        self._gmt_create_end = None
        self._gmt_create_start = None
        self._invoice_status = None
        self._invoice_type = None
        self._out_request_no_list = None
        self._page_no = None
        self._page_size = None
        self._query_mode = None
        self._saas_invoice_order_no_list = None

    @property
    def gmt_create_end(self):
        return self._gmt_create_end

    @gmt_create_end.setter
    def gmt_create_end(self, value):
        self._gmt_create_end = value
    @property
    def gmt_create_start(self):
        return self._gmt_create_start

    @gmt_create_start.setter
    def gmt_create_start(self, value):
        self._gmt_create_start = value
    @property
    def invoice_status(self):
        return self._invoice_status

    @invoice_status.setter
    def invoice_status(self, value):
        self._invoice_status = value
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def out_request_no_list(self):
        return self._out_request_no_list

    @out_request_no_list.setter
    def out_request_no_list(self, value):
        if isinstance(value, list):
            self._out_request_no_list = list()
            for i in value:
                self._out_request_no_list.append(i)
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def query_mode(self):
        return self._query_mode

    @query_mode.setter
    def query_mode(self, value):
        self._query_mode = value
    @property
    def saas_invoice_order_no_list(self):
        return self._saas_invoice_order_no_list

    @saas_invoice_order_no_list.setter
    def saas_invoice_order_no_list(self, value):
        if isinstance(value, list):
            self._saas_invoice_order_no_list = list()
            for i in value:
                self._saas_invoice_order_no_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_create_end:
            if hasattr(self.gmt_create_end, 'to_alipay_dict'):
                params['gmt_create_end'] = self.gmt_create_end.to_alipay_dict()
            else:
                params['gmt_create_end'] = self.gmt_create_end
        if self.gmt_create_start:
            if hasattr(self.gmt_create_start, 'to_alipay_dict'):
                params['gmt_create_start'] = self.gmt_create_start.to_alipay_dict()
            else:
                params['gmt_create_start'] = self.gmt_create_start
        if self.invoice_status:
            if hasattr(self.invoice_status, 'to_alipay_dict'):
                params['invoice_status'] = self.invoice_status.to_alipay_dict()
            else:
                params['invoice_status'] = self.invoice_status
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.out_request_no_list:
            if isinstance(self.out_request_no_list, list):
                for i in range(0, len(self.out_request_no_list)):
                    element = self.out_request_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_request_no_list[i] = element.to_alipay_dict()
            if hasattr(self.out_request_no_list, 'to_alipay_dict'):
                params['out_request_no_list'] = self.out_request_no_list.to_alipay_dict()
            else:
                params['out_request_no_list'] = self.out_request_no_list
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.query_mode:
            if hasattr(self.query_mode, 'to_alipay_dict'):
                params['query_mode'] = self.query_mode.to_alipay_dict()
            else:
                params['query_mode'] = self.query_mode
        if self.saas_invoice_order_no_list:
            if isinstance(self.saas_invoice_order_no_list, list):
                for i in range(0, len(self.saas_invoice_order_no_list)):
                    element = self.saas_invoice_order_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.saas_invoice_order_no_list[i] = element.to_alipay_dict()
            if hasattr(self.saas_invoice_order_no_list, 'to_alipay_dict'):
                params['saas_invoice_order_no_list'] = self.saas_invoice_order_no_list.to_alipay_dict()
            else:
                params['saas_invoice_order_no_list'] = self.saas_invoice_order_no_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeSaasInvoiceBatchqueryModel()
        if 'gmt_create_end' in d:
            o.gmt_create_end = d['gmt_create_end']
        if 'gmt_create_start' in d:
            o.gmt_create_start = d['gmt_create_start']
        if 'invoice_status' in d:
            o.invoice_status = d['invoice_status']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'out_request_no_list' in d:
            o.out_request_no_list = d['out_request_no_list']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'query_mode' in d:
            o.query_mode = d['query_mode']
        if 'saas_invoice_order_no_list' in d:
            o.saas_invoice_order_no_list = d['saas_invoice_order_no_list']
        return o


