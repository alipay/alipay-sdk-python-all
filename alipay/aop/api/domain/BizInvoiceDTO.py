#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BizInvoiceDTO(object):

    def __init__(self):
        self._amount = None
        self._excluding_tax_amount = None
        self._invoice_code = None
        self._invoice_date = None
        self._invoice_no = None
        self._invoice_type = None
        self._invoice_urls = None
        self._red = None
        self._tax_amount = None
        self._tax_rate = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def excluding_tax_amount(self):
        return self._excluding_tax_amount

    @excluding_tax_amount.setter
    def excluding_tax_amount(self, value):
        self._excluding_tax_amount = value
    @property
    def invoice_code(self):
        return self._invoice_code

    @invoice_code.setter
    def invoice_code(self, value):
        self._invoice_code = value
    @property
    def invoice_date(self):
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, value):
        self._invoice_date = value
    @property
    def invoice_no(self):
        return self._invoice_no

    @invoice_no.setter
    def invoice_no(self, value):
        self._invoice_no = value
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def invoice_urls(self):
        return self._invoice_urls

    @invoice_urls.setter
    def invoice_urls(self, value):
        if isinstance(value, list):
            self._invoice_urls = list()
            for i in value:
                self._invoice_urls.append(i)
    @property
    def red(self):
        return self._red

    @red.setter
    def red(self, value):
        self._red = value
    @property
    def tax_amount(self):
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, value):
        self._tax_amount = value
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.excluding_tax_amount:
            if hasattr(self.excluding_tax_amount, 'to_alipay_dict'):
                params['excluding_tax_amount'] = self.excluding_tax_amount.to_alipay_dict()
            else:
                params['excluding_tax_amount'] = self.excluding_tax_amount
        if self.invoice_code:
            if hasattr(self.invoice_code, 'to_alipay_dict'):
                params['invoice_code'] = self.invoice_code.to_alipay_dict()
            else:
                params['invoice_code'] = self.invoice_code
        if self.invoice_date:
            if hasattr(self.invoice_date, 'to_alipay_dict'):
                params['invoice_date'] = self.invoice_date.to_alipay_dict()
            else:
                params['invoice_date'] = self.invoice_date
        if self.invoice_no:
            if hasattr(self.invoice_no, 'to_alipay_dict'):
                params['invoice_no'] = self.invoice_no.to_alipay_dict()
            else:
                params['invoice_no'] = self.invoice_no
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.invoice_urls:
            if isinstance(self.invoice_urls, list):
                for i in range(0, len(self.invoice_urls)):
                    element = self.invoice_urls[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_urls[i] = element.to_alipay_dict()
            if hasattr(self.invoice_urls, 'to_alipay_dict'):
                params['invoice_urls'] = self.invoice_urls.to_alipay_dict()
            else:
                params['invoice_urls'] = self.invoice_urls
        if self.red:
            if hasattr(self.red, 'to_alipay_dict'):
                params['red'] = self.red.to_alipay_dict()
            else:
                params['red'] = self.red
        if self.tax_amount:
            if hasattr(self.tax_amount, 'to_alipay_dict'):
                params['tax_amount'] = self.tax_amount.to_alipay_dict()
            else:
                params['tax_amount'] = self.tax_amount
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BizInvoiceDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'excluding_tax_amount' in d:
            o.excluding_tax_amount = d['excluding_tax_amount']
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_date' in d:
            o.invoice_date = d['invoice_date']
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'invoice_urls' in d:
            o.invoice_urls = d['invoice_urls']
        if 'red' in d:
            o.red = d['red']
        if 'tax_amount' in d:
            o.tax_amount = d['tax_amount']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        return o


