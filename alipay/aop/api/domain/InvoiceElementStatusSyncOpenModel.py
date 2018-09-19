#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceElementStatusSyncOpenModel(object):

    def __init__(self):
        self._apply_id = None
        self._expense_detail_url = None
        self._invoice_code = None
        self._invoice_no = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def expense_detail_url(self):
        return self._expense_detail_url

    @expense_detail_url.setter
    def expense_detail_url(self, value):
        self._expense_detail_url = value
    @property
    def invoice_code(self):
        return self._invoice_code

    @invoice_code.setter
    def invoice_code(self, value):
        self._invoice_code = value
    @property
    def invoice_no(self):
        return self._invoice_no

    @invoice_no.setter
    def invoice_no(self, value):
        self._invoice_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
        if self.expense_detail_url:
            if hasattr(self.expense_detail_url, 'to_alipay_dict'):
                params['expense_detail_url'] = self.expense_detail_url.to_alipay_dict()
            else:
                params['expense_detail_url'] = self.expense_detail_url
        if self.invoice_code:
            if hasattr(self.invoice_code, 'to_alipay_dict'):
                params['invoice_code'] = self.invoice_code.to_alipay_dict()
            else:
                params['invoice_code'] = self.invoice_code
        if self.invoice_no:
            if hasattr(self.invoice_no, 'to_alipay_dict'):
                params['invoice_no'] = self.invoice_no.to_alipay_dict()
            else:
                params['invoice_no'] = self.invoice_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceElementStatusSyncOpenModel()
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'expense_detail_url' in d:
            o.expense_detail_url = d['expense_detail_url']
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        return o


