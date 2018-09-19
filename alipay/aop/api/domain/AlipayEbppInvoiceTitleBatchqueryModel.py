#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceTitleBatchqueryModel(object):

    def __init__(self):
        self._end_invoice_date = None
        self._expense_status_list = None
        self._invoice_kind_list = None
        self._limit_size = None
        self._page_num = None
        self._start_invoice_date = None
        self._title_name = None

    @property
    def end_invoice_date(self):
        return self._end_invoice_date

    @end_invoice_date.setter
    def end_invoice_date(self, value):
        self._end_invoice_date = value
    @property
    def expense_status_list(self):
        return self._expense_status_list

    @expense_status_list.setter
    def expense_status_list(self, value):
        if isinstance(value, list):
            self._expense_status_list = list()
            for i in value:
                self._expense_status_list.append(i)
    @property
    def invoice_kind_list(self):
        return self._invoice_kind_list

    @invoice_kind_list.setter
    def invoice_kind_list(self, value):
        if isinstance(value, list):
            self._invoice_kind_list = list()
            for i in value:
                self._invoice_kind_list.append(i)
    @property
    def limit_size(self):
        return self._limit_size

    @limit_size.setter
    def limit_size(self, value):
        self._limit_size = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def start_invoice_date(self):
        return self._start_invoice_date

    @start_invoice_date.setter
    def start_invoice_date(self, value):
        self._start_invoice_date = value
    @property
    def title_name(self):
        return self._title_name

    @title_name.setter
    def title_name(self, value):
        self._title_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_invoice_date:
            if hasattr(self.end_invoice_date, 'to_alipay_dict'):
                params['end_invoice_date'] = self.end_invoice_date.to_alipay_dict()
            else:
                params['end_invoice_date'] = self.end_invoice_date
        if self.expense_status_list:
            if isinstance(self.expense_status_list, list):
                for i in range(0, len(self.expense_status_list)):
                    element = self.expense_status_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.expense_status_list[i] = element.to_alipay_dict()
            if hasattr(self.expense_status_list, 'to_alipay_dict'):
                params['expense_status_list'] = self.expense_status_list.to_alipay_dict()
            else:
                params['expense_status_list'] = self.expense_status_list
        if self.invoice_kind_list:
            if isinstance(self.invoice_kind_list, list):
                for i in range(0, len(self.invoice_kind_list)):
                    element = self.invoice_kind_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_kind_list[i] = element.to_alipay_dict()
            if hasattr(self.invoice_kind_list, 'to_alipay_dict'):
                params['invoice_kind_list'] = self.invoice_kind_list.to_alipay_dict()
            else:
                params['invoice_kind_list'] = self.invoice_kind_list
        if self.limit_size:
            if hasattr(self.limit_size, 'to_alipay_dict'):
                params['limit_size'] = self.limit_size.to_alipay_dict()
            else:
                params['limit_size'] = self.limit_size
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.start_invoice_date:
            if hasattr(self.start_invoice_date, 'to_alipay_dict'):
                params['start_invoice_date'] = self.start_invoice_date.to_alipay_dict()
            else:
                params['start_invoice_date'] = self.start_invoice_date
        if self.title_name:
            if hasattr(self.title_name, 'to_alipay_dict'):
                params['title_name'] = self.title_name.to_alipay_dict()
            else:
                params['title_name'] = self.title_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceTitleBatchqueryModel()
        if 'end_invoice_date' in d:
            o.end_invoice_date = d['end_invoice_date']
        if 'expense_status_list' in d:
            o.expense_status_list = d['expense_status_list']
        if 'invoice_kind_list' in d:
            o.invoice_kind_list = d['invoice_kind_list']
        if 'limit_size' in d:
            o.limit_size = d['limit_size']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'start_invoice_date' in d:
            o.start_invoice_date = d['start_invoice_date']
        if 'title_name' in d:
            o.title_name = d['title_name']
        return o


