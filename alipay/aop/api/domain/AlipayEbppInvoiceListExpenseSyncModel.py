#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceElementStatusSyncOpenModel import InvoiceElementStatusSyncOpenModel


class AlipayEbppInvoiceListExpenseSyncModel(object):

    def __init__(self):
        self._business_time = None
        self._expense_order_no = None
        self._expense_tax_no = None
        self._invoice_element_list = None
        self._memo = None
        self._status = None
        self._user_id = None

    @property
    def business_time(self):
        return self._business_time

    @business_time.setter
    def business_time(self, value):
        self._business_time = value
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
    def invoice_element_list(self):
        return self._invoice_element_list

    @invoice_element_list.setter
    def invoice_element_list(self, value):
        if isinstance(value, list):
            self._invoice_element_list = list()
            for i in value:
                if isinstance(i, InvoiceElementStatusSyncOpenModel):
                    self._invoice_element_list.append(i)
                else:
                    self._invoice_element_list.append(InvoiceElementStatusSyncOpenModel.from_alipay_dict(i))
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
        if self.business_time:
            if hasattr(self.business_time, 'to_alipay_dict'):
                params['business_time'] = self.business_time.to_alipay_dict()
            else:
                params['business_time'] = self.business_time
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
        if self.invoice_element_list:
            if isinstance(self.invoice_element_list, list):
                for i in range(0, len(self.invoice_element_list)):
                    element = self.invoice_element_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_element_list[i] = element.to_alipay_dict()
            if hasattr(self.invoice_element_list, 'to_alipay_dict'):
                params['invoice_element_list'] = self.invoice_element_list.to_alipay_dict()
            else:
                params['invoice_element_list'] = self.invoice_element_list
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
        o = AlipayEbppInvoiceListExpenseSyncModel()
        if 'business_time' in d:
            o.business_time = d['business_time']
        if 'expense_order_no' in d:
            o.expense_order_no = d['expense_order_no']
        if 'expense_tax_no' in d:
            o.expense_tax_no = d['expense_tax_no']
        if 'invoice_element_list' in d:
            o.invoice_element_list = d['invoice_element_list']
        if 'memo' in d:
            o.memo = d['memo']
        if 'status' in d:
            o.status = d['status']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


