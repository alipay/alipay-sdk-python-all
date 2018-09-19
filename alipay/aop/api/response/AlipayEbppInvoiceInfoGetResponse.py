#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InvoiceModelContent import InvoiceModelContent


class AlipayEbppInvoiceInfoGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceInfoGetResponse, self).__init__()
        self._invoice_model = None

    @property
    def invoice_model(self):
        return self._invoice_model

    @invoice_model.setter
    def invoice_model(self, value):
        if isinstance(value, InvoiceModelContent):
            self._invoice_model = value
        else:
            self._invoice_model = InvoiceModelContent.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceInfoGetResponse, self).parse_response_content(response_content)
        if 'invoice_model' in response:
            self.invoice_model = response['invoice_model']
