#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceKeyInfo(object):

    def __init__(self):
        self._invoice_merchant_name = None
        self._is_support_invoice = None
        self._tax_num = None

    @property
    def invoice_merchant_name(self):
        return self._invoice_merchant_name

    @invoice_merchant_name.setter
    def invoice_merchant_name(self, value):
        self._invoice_merchant_name = value
    @property
    def is_support_invoice(self):
        return self._is_support_invoice

    @is_support_invoice.setter
    def is_support_invoice(self, value):
        self._is_support_invoice = value
    @property
    def tax_num(self):
        return self._tax_num

    @tax_num.setter
    def tax_num(self, value):
        self._tax_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.invoice_merchant_name:
            if hasattr(self.invoice_merchant_name, 'to_alipay_dict'):
                params['invoice_merchant_name'] = self.invoice_merchant_name.to_alipay_dict()
            else:
                params['invoice_merchant_name'] = self.invoice_merchant_name
        if self.is_support_invoice:
            if hasattr(self.is_support_invoice, 'to_alipay_dict'):
                params['is_support_invoice'] = self.is_support_invoice.to_alipay_dict()
            else:
                params['is_support_invoice'] = self.is_support_invoice
        if self.tax_num:
            if hasattr(self.tax_num, 'to_alipay_dict'):
                params['tax_num'] = self.tax_num.to_alipay_dict()
            else:
                params['tax_num'] = self.tax_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceKeyInfo()
        if 'invoice_merchant_name' in d:
            o.invoice_merchant_name = d['invoice_merchant_name']
        if 'is_support_invoice' in d:
            o.is_support_invoice = d['is_support_invoice']
        if 'tax_num' in d:
            o.tax_num = d['tax_num']
        return o


