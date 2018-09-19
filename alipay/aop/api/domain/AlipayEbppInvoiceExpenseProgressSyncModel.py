#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceExpenseProgressSyncModel(object):

    def __init__(self):
        self._apply_id = None
        self._business_time = None
        self._expense_detail_url = None
        self._expense_order_no = None
        self._expense_tax_no = None
        self._invoice_code = None
        self._invoice_no = None
        self._memo = None
        self._status = None
        self._user_id = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def business_time(self):
        return self._business_time

    @business_time.setter
    def business_time(self, value):
        self._business_time = value
    @property
    def expense_detail_url(self):
        return self._expense_detail_url

    @expense_detail_url.setter
    def expense_detail_url(self, value):
        self._expense_detail_url = value
    @property
    def expense_order_no(self):
        return self._expense_order_no

    @expense_order_no.setter
    def expense_order_no(self, value):
        self._expense_order_no = value
    @property
    def expense_tax_no(self):
        return self._expense_tax_no

    @expense_tax_no.setter
    def expense_tax_no(self, value):
        self._expense_tax_no = value
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
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
        if self.business_time:
            if hasattr(self.business_time, 'to_alipay_dict'):
                params['business_time'] = self.business_time.to_alipay_dict()
            else:
                params['business_time'] = self.business_time
        if self.expense_detail_url:
            if hasattr(self.expense_detail_url, 'to_alipay_dict'):
                params['expense_detail_url'] = self.expense_detail_url.to_alipay_dict()
            else:
                params['expense_detail_url'] = self.expense_detail_url
        if self.expense_order_no:
            if hasattr(self.expense_order_no, 'to_alipay_dict'):
                params['expense_order_no'] = self.expense_order_no.to_alipay_dict()
            else:
                params['expense_order_no'] = self.expense_order_no
        if self.expense_tax_no:
            if hasattr(self.expense_tax_no, 'to_alipay_dict'):
                params['expense_tax_no'] = self.expense_tax_no.to_alipay_dict()
            else:
                params['expense_tax_no'] = self.expense_tax_no
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
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceExpenseProgressSyncModel()
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'business_time' in d:
            o.business_time = d['business_time']
        if 'expense_detail_url' in d:
            o.expense_detail_url = d['expense_detail_url']
        if 'expense_order_no' in d:
            o.expense_order_no = d['expense_order_no']
        if 'expense_tax_no' in d:
            o.expense_tax_no = d['expense_tax_no']
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        if 'memo' in d:
            o.memo = d['memo']
        if 'status' in d:
            o.status = d['status']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


