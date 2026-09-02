#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InvoiceDetailInfo import InvoiceDetailInfo


class AlipayTradeSaasInvoiceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSaasInvoiceQueryResponse, self).__init__()
        self._invoice_detail_info = None

    @property
    def invoice_detail_info(self):
        return self._invoice_detail_info

    @invoice_detail_info.setter
    def invoice_detail_info(self, value):
        if isinstance(value, InvoiceDetailInfo):
            self._invoice_detail_info = value
        else:
            self._invoice_detail_info = InvoiceDetailInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSaasInvoiceQueryResponse, self).parse_response_content(response_content)
        if 'invoice_detail_info' in response:
            self.invoice_detail_info = response['invoice_detail_info']
