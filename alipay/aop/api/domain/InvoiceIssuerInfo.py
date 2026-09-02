#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceIssuerInfo(object):

    def __init__(self):
        self._cashier_name = None
        self._checker_name = None
        self._invoice_clerk_certificate_no = None
        self._invoice_clerk_certificate_type = None
        self._invoice_issuer = None

    @property
    def cashier_name(self):
        return self._cashier_name

    @cashier_name.setter
    def cashier_name(self, value):
        self._cashier_name = value
    @property
    def checker_name(self):
        return self._checker_name

    @checker_name.setter
    def checker_name(self, value):
        self._checker_name = value
    @property
    def invoice_clerk_certificate_no(self):
        return self._invoice_clerk_certificate_no

    @invoice_clerk_certificate_no.setter
    def invoice_clerk_certificate_no(self, value):
        self._invoice_clerk_certificate_no = value
    @property
    def invoice_clerk_certificate_type(self):
        return self._invoice_clerk_certificate_type

    @invoice_clerk_certificate_type.setter
    def invoice_clerk_certificate_type(self, value):
        self._invoice_clerk_certificate_type = value
    @property
    def invoice_issuer(self):
        return self._invoice_issuer

    @invoice_issuer.setter
    def invoice_issuer(self, value):
        self._invoice_issuer = value


    def to_alipay_dict(self):
        params = dict()
        if self.cashier_name:
            if hasattr(self.cashier_name, 'to_alipay_dict'):
                params['cashier_name'] = self.cashier_name.to_alipay_dict()
            else:
                params['cashier_name'] = self.cashier_name
        if self.checker_name:
            if hasattr(self.checker_name, 'to_alipay_dict'):
                params['checker_name'] = self.checker_name.to_alipay_dict()
            else:
                params['checker_name'] = self.checker_name
        if self.invoice_clerk_certificate_no:
            if hasattr(self.invoice_clerk_certificate_no, 'to_alipay_dict'):
                params['invoice_clerk_certificate_no'] = self.invoice_clerk_certificate_no.to_alipay_dict()
            else:
                params['invoice_clerk_certificate_no'] = self.invoice_clerk_certificate_no
        if self.invoice_clerk_certificate_type:
            if hasattr(self.invoice_clerk_certificate_type, 'to_alipay_dict'):
                params['invoice_clerk_certificate_type'] = self.invoice_clerk_certificate_type.to_alipay_dict()
            else:
                params['invoice_clerk_certificate_type'] = self.invoice_clerk_certificate_type
        if self.invoice_issuer:
            if hasattr(self.invoice_issuer, 'to_alipay_dict'):
                params['invoice_issuer'] = self.invoice_issuer.to_alipay_dict()
            else:
                params['invoice_issuer'] = self.invoice_issuer
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceIssuerInfo()
        if 'cashier_name' in d:
            o.cashier_name = d['cashier_name']
        if 'checker_name' in d:
            o.checker_name = d['checker_name']
        if 'invoice_clerk_certificate_no' in d:
            o.invoice_clerk_certificate_no = d['invoice_clerk_certificate_no']
        if 'invoice_clerk_certificate_type' in d:
            o.invoice_clerk_certificate_type = d['invoice_clerk_certificate_type']
        if 'invoice_issuer' in d:
            o.invoice_issuer = d['invoice_issuer']
        return o


