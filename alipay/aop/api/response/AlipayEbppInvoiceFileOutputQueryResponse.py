#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInvoiceFileOutputQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceFileOutputQueryResponse, self).__init__()
        self._file_type = None
        self._invoice_file_content = None

    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def invoice_file_content(self):
        return self._invoice_file_content

    @invoice_file_content.setter
    def invoice_file_content(self, value):
        self._invoice_file_content = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceFileOutputQueryResponse, self).parse_response_content(response_content)
        if 'file_type' in response:
            self.file_type = response['file_type']
        if 'invoice_file_content' in response:
            self.invoice_file_content = response['invoice_file_content']
