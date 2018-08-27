#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InvoiceQueryOpenModel import InvoiceQueryOpenModel


class AlipayEbppInvoiceInfoApplyidQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceInfoApplyidQueryResponse, self).__init__()
        self._invoice_info = None

    @property
    def invoice_info(self):
        return self._invoice_info

    @invoice_info.setter
    def invoice_info(self, value):
        if isinstance(value, list):
            self._invoice_info = list()
            for i in value:
                if isinstance(i, InvoiceQueryOpenModel):
                    self._invoice_info.append(i)
                else:
                    self._invoice_info.append(InvoiceQueryOpenModel.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceInfoApplyidQueryResponse, self).parse_response_content(response_content)
        if 'invoice_info' in response:
            self.invoice_info = response['invoice_info']
