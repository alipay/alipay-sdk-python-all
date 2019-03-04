#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceFinancialBlockchainBatchqueryModel(object):

    def __init__(self):
        self._cert_no_hash = None
        self._cert_type = None
        self._current_page = None
        self._invoice_kind = None
        self._page_size = None

    @property
    def cert_no_hash(self):
        return self._cert_no_hash

    @cert_no_hash.setter
    def cert_no_hash(self, value):
        self._cert_no_hash = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def invoice_kind(self):
        return self._invoice_kind

    @invoice_kind.setter
    def invoice_kind(self, value):
        self._invoice_kind = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no_hash:
            if hasattr(self.cert_no_hash, 'to_alipay_dict'):
                params['cert_no_hash'] = self.cert_no_hash.to_alipay_dict()
            else:
                params['cert_no_hash'] = self.cert_no_hash
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.current_page:
            if hasattr(self.current_page, 'to_alipay_dict'):
                params['current_page'] = self.current_page.to_alipay_dict()
            else:
                params['current_page'] = self.current_page
        if self.invoice_kind:
            if hasattr(self.invoice_kind, 'to_alipay_dict'):
                params['invoice_kind'] = self.invoice_kind.to_alipay_dict()
            else:
                params['invoice_kind'] = self.invoice_kind
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceFinancialBlockchainBatchqueryModel()
        if 'cert_no_hash' in d:
            o.cert_no_hash = d['cert_no_hash']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'current_page' in d:
            o.current_page = d['current_page']
        if 'invoice_kind' in d:
            o.invoice_kind = d['invoice_kind']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


