#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FinanceFileInfo import FinanceFileInfo


class FinanceInvoiceInfo(object):

    def __init__(self):
        self._amount = None
        self._amount_with_tax = None
        self._billing_date = None
        self._check_code = None
        self._contract_no = None
        self._file = None
        self._invoice_code = None
        self._invoice_number = None
        self._invoice_type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def amount_with_tax(self):
        return self._amount_with_tax

    @amount_with_tax.setter
    def amount_with_tax(self, value):
        self._amount_with_tax = value
    @property
    def billing_date(self):
        return self._billing_date

    @billing_date.setter
    def billing_date(self, value):
        self._billing_date = value
    @property
    def check_code(self):
        return self._check_code

    @check_code.setter
    def check_code(self, value):
        self._check_code = value
    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def file(self):
        return self._file

    @file.setter
    def file(self, value):
        if isinstance(value, FinanceFileInfo):
            self._file = value
        else:
            self._file = FinanceFileInfo.from_alipay_dict(value)
    @property
    def invoice_code(self):
        return self._invoice_code

    @invoice_code.setter
    def invoice_code(self, value):
        self._invoice_code = value
    @property
    def invoice_number(self):
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, value):
        self._invoice_number = value
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.amount_with_tax:
            if hasattr(self.amount_with_tax, 'to_alipay_dict'):
                params['amount_with_tax'] = self.amount_with_tax.to_alipay_dict()
            else:
                params['amount_with_tax'] = self.amount_with_tax
        if self.billing_date:
            if hasattr(self.billing_date, 'to_alipay_dict'):
                params['billing_date'] = self.billing_date.to_alipay_dict()
            else:
                params['billing_date'] = self.billing_date
        if self.check_code:
            if hasattr(self.check_code, 'to_alipay_dict'):
                params['check_code'] = self.check_code.to_alipay_dict()
            else:
                params['check_code'] = self.check_code
        if self.contract_no:
            if hasattr(self.contract_no, 'to_alipay_dict'):
                params['contract_no'] = self.contract_no.to_alipay_dict()
            else:
                params['contract_no'] = self.contract_no
        if self.file:
            if hasattr(self.file, 'to_alipay_dict'):
                params['file'] = self.file.to_alipay_dict()
            else:
                params['file'] = self.file
        if self.invoice_code:
            if hasattr(self.invoice_code, 'to_alipay_dict'):
                params['invoice_code'] = self.invoice_code.to_alipay_dict()
            else:
                params['invoice_code'] = self.invoice_code
        if self.invoice_number:
            if hasattr(self.invoice_number, 'to_alipay_dict'):
                params['invoice_number'] = self.invoice_number.to_alipay_dict()
            else:
                params['invoice_number'] = self.invoice_number
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FinanceInvoiceInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'amount_with_tax' in d:
            o.amount_with_tax = d['amount_with_tax']
        if 'billing_date' in d:
            o.billing_date = d['billing_date']
        if 'check_code' in d:
            o.check_code = d['check_code']
        if 'contract_no' in d:
            o.contract_no = d['contract_no']
        if 'file' in d:
            o.file = d['file']
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_number' in d:
            o.invoice_number = d['invoice_number']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        return o


