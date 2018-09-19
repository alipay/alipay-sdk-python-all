#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneInvoiceApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneInvoiceApplyResponse, self).__init__()
        self._invoice_apply_no = None
        self._out_request_no = None

    @property
    def invoice_apply_no(self):
        return self._invoice_apply_no

    @invoice_apply_no.setter
    def invoice_apply_no(self, value):
        self._invoice_apply_no = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneInvoiceApplyResponse, self).parse_response_content(response_content)
        if 'invoice_apply_no' in response:
            self.invoice_apply_no = response['invoice_apply_no']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
