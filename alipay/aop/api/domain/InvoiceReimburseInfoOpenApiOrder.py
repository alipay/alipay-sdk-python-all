#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AccountInfoOpenApiOrder import AccountInfoOpenApiOrder


class InvoiceReimburseInfoOpenApiOrder(object):

    def __init__(self):
        self._account_info_order_list = None
        self._bill_no = None
        self._currency = None
        self._line_no = None
        self._use_amt = None

    @property
    def account_info_order_list(self):
        return self._account_info_order_list

    @account_info_order_list.setter
    def account_info_order_list(self, value):
        if isinstance(value, list):
            self._account_info_order_list = list()
            for i in value:
                if isinstance(i, AccountInfoOpenApiOrder):
                    self._account_info_order_list.append(i)
                else:
                    self._account_info_order_list.append(AccountInfoOpenApiOrder.from_alipay_dict(i))
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def line_no(self):
        return self._line_no

    @line_no.setter
    def line_no(self, value):
        self._line_no = value
    @property
    def use_amt(self):
        return self._use_amt

    @use_amt.setter
    def use_amt(self, value):
        self._use_amt = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_info_order_list:
            if isinstance(self.account_info_order_list, list):
                for i in range(0, len(self.account_info_order_list)):
                    element = self.account_info_order_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.account_info_order_list[i] = element.to_alipay_dict()
            if hasattr(self.account_info_order_list, 'to_alipay_dict'):
                params['account_info_order_list'] = self.account_info_order_list.to_alipay_dict()
            else:
                params['account_info_order_list'] = self.account_info_order_list
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.line_no:
            if hasattr(self.line_no, 'to_alipay_dict'):
                params['line_no'] = self.line_no.to_alipay_dict()
            else:
                params['line_no'] = self.line_no
        if self.use_amt:
            if hasattr(self.use_amt, 'to_alipay_dict'):
                params['use_amt'] = self.use_amt.to_alipay_dict()
            else:
                params['use_amt'] = self.use_amt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceReimburseInfoOpenApiOrder()
        if 'account_info_order_list' in d:
            o.account_info_order_list = d['account_info_order_list']
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'currency' in d:
            o.currency = d['currency']
        if 'line_no' in d:
            o.line_no = d['line_no']
        if 'use_amt' in d:
            o.use_amt = d['use_amt']
        return o


