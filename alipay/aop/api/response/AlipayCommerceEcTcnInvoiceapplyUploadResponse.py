#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcTcnInvoiceapplyUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcTcnInvoiceapplyUploadResponse, self).__init__()
        self._apply_id = None
        self._invoice_code = None
        self._invoice_no = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcTcnInvoiceapplyUploadResponse, self).parse_response_content(response_content)
        if 'apply_id' in response:
            self.apply_id = response['apply_id']
        if 'invoice_code' in response:
            self.invoice_code = response['invoice_code']
        if 'invoice_no' in response:
            self.invoice_no = response['invoice_no']
