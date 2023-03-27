#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoicingNoAndDate(object):

    def __init__(self):
        self._invoice_no = None
        self._invoicing_date = None

    @property
    def invoice_no(self):
        return self._invoice_no

    @invoice_no.setter
    def invoice_no(self, value):
        self._invoice_no = value
    @property
    def invoicing_date(self):
        return self._invoicing_date

    @invoicing_date.setter
    def invoicing_date(self, value):
        self._invoicing_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.invoice_no:
            if hasattr(self.invoice_no, 'to_alipay_dict'):
                params['invoice_no'] = self.invoice_no.to_alipay_dict()
            else:
                params['invoice_no'] = self.invoice_no
        if self.invoicing_date:
            if hasattr(self.invoicing_date, 'to_alipay_dict'):
                params['invoicing_date'] = self.invoicing_date.to_alipay_dict()
            else:
                params['invoicing_date'] = self.invoicing_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoicingNoAndDate()
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        if 'invoicing_date' in d:
            o.invoicing_date = d['invoicing_date']
        return o


