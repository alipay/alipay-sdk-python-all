#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInvoiceMerchantApplyUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceMerchantApplyUploadResponse, self).__init__()
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

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceMerchantApplyUploadResponse, self).parse_response_content(response_content)
        if 'invoice_code' in response:
            self.invoice_code = response['invoice_code']
        if 'invoice_no' in response:
            self.invoice_no = response['invoice_no']
