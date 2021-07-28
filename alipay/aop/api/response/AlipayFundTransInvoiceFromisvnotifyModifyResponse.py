#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundTransInvoiceFromisvnotifyModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTransInvoiceFromisvnotifyModifyResponse, self).__init__()
        self._invoice_url = None

    @property
    def invoice_url(self):
        return self._invoice_url

    @invoice_url.setter
    def invoice_url(self, value):
        self._invoice_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundTransInvoiceFromisvnotifyModifyResponse, self).parse_response_content(response_content)
        if 'invoice_url' in response:
            self.invoice_url = response['invoice_url']
