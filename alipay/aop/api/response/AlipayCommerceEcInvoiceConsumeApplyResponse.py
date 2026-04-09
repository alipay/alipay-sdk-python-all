#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcInvoiceConsumeApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcInvoiceConsumeApplyResponse, self).__init__()
        self._invoice_apply_id = None

    @property
    def invoice_apply_id(self):
        return self._invoice_apply_id

    @invoice_apply_id.setter
    def invoice_apply_id(self, value):
        self._invoice_apply_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcInvoiceConsumeApplyResponse, self).parse_response_content(response_content)
        if 'invoice_apply_id' in response:
            self.invoice_apply_id = response['invoice_apply_id']
