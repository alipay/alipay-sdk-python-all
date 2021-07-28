#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExpenseConsumeInfo import ExpenseConsumeInfo
from alipay.aop.api.domain.ExpenseConsumeInfo import ExpenseConsumeInfo
from alipay.aop.api.domain.ExpenseInvoiceInfo import ExpenseInvoiceInfo


class ExpenseCtrlConsumeInfo(object):

    def __init__(self):
        self._expense_consume_info = None
        self._related_enterprise_consume_list = None
        self._related_enterprise_invoice_list = None

    @property
    def expense_consume_info(self):
        return self._expense_consume_info

    @expense_consume_info.setter
    def expense_consume_info(self, value):
        if isinstance(value, ExpenseConsumeInfo):
            self._expense_consume_info = value
        else:
            self._expense_consume_info = ExpenseConsumeInfo.from_alipay_dict(value)
    @property
    def related_enterprise_consume_list(self):
        return self._related_enterprise_consume_list

    @related_enterprise_consume_list.setter
    def related_enterprise_consume_list(self, value):
        if isinstance(value, list):
            self._related_enterprise_consume_list = list()
            for i in value:
                if isinstance(i, ExpenseConsumeInfo):
                    self._related_enterprise_consume_list.append(i)
                else:
                    self._related_enterprise_consume_list.append(ExpenseConsumeInfo.from_alipay_dict(i))
    @property
    def related_enterprise_invoice_list(self):
        return self._related_enterprise_invoice_list

    @related_enterprise_invoice_list.setter
    def related_enterprise_invoice_list(self, value):
        if isinstance(value, list):
            self._related_enterprise_invoice_list = list()
            for i in value:
                if isinstance(i, ExpenseInvoiceInfo):
                    self._related_enterprise_invoice_list.append(i)
                else:
                    self._related_enterprise_invoice_list.append(ExpenseInvoiceInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.expense_consume_info:
            if hasattr(self.expense_consume_info, 'to_alipay_dict'):
                params['expense_consume_info'] = self.expense_consume_info.to_alipay_dict()
            else:
                params['expense_consume_info'] = self.expense_consume_info
        if self.related_enterprise_consume_list:
            if isinstance(self.related_enterprise_consume_list, list):
                for i in range(0, len(self.related_enterprise_consume_list)):
                    element = self.related_enterprise_consume_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.related_enterprise_consume_list[i] = element.to_alipay_dict()
            if hasattr(self.related_enterprise_consume_list, 'to_alipay_dict'):
                params['related_enterprise_consume_list'] = self.related_enterprise_consume_list.to_alipay_dict()
            else:
                params['related_enterprise_consume_list'] = self.related_enterprise_consume_list
        if self.related_enterprise_invoice_list:
            if isinstance(self.related_enterprise_invoice_list, list):
                for i in range(0, len(self.related_enterprise_invoice_list)):
                    element = self.related_enterprise_invoice_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.related_enterprise_invoice_list[i] = element.to_alipay_dict()
            if hasattr(self.related_enterprise_invoice_list, 'to_alipay_dict'):
                params['related_enterprise_invoice_list'] = self.related_enterprise_invoice_list.to_alipay_dict()
            else:
                params['related_enterprise_invoice_list'] = self.related_enterprise_invoice_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExpenseCtrlConsumeInfo()
        if 'expense_consume_info' in d:
            o.expense_consume_info = d['expense_consume_info']
        if 'related_enterprise_consume_list' in d:
            o.related_enterprise_consume_list = d['related_enterprise_consume_list']
        if 'related_enterprise_invoice_list' in d:
            o.related_enterprise_invoice_list = d['related_enterprise_invoice_list']
        return o


