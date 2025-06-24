#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InvoiceData import InvoiceData


class AlipayCloudCloudbaseInvoiceStatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseInvoiceStatusQueryResponse, self).__init__()
        self._biz_trace_id = None
        self._invoice_data = None
        self._message = None

    @property
    def biz_trace_id(self):
        return self._biz_trace_id

    @biz_trace_id.setter
    def biz_trace_id(self, value):
        self._biz_trace_id = value
    @property
    def invoice_data(self):
        return self._invoice_data

    @invoice_data.setter
    def invoice_data(self, value):
        if isinstance(value, InvoiceData):
            self._invoice_data = value
        else:
            self._invoice_data = InvoiceData.from_alipay_dict(value)
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseInvoiceStatusQueryResponse, self).parse_response_content(response_content)
        if 'biz_trace_id' in response:
            self.biz_trace_id = response['biz_trace_id']
        if 'invoice_data' in response:
            self.invoice_data = response['invoice_data']
        if 'message' in response:
            self.message = response['message']
