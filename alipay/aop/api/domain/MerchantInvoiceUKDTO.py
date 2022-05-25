#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantInvoiceUKDTO(object):

    def __init__(self):
        self._invoice_code = None
        self._invoice_no = None

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


    def to_alipay_dict(self):
        params = dict()
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantInvoiceUKDTO()
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        return o


