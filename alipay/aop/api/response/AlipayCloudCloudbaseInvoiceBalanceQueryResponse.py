#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InvoiceAmountInfo import InvoiceAmountInfo


class AlipayCloudCloudbaseInvoiceBalanceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseInvoiceBalanceQueryResponse, self).__init__()
        self._biz_trace_id = None
        self._invoice_amount_info = None
        self._message = None

    @property
    def biz_trace_id(self):
        return self._biz_trace_id

    @biz_trace_id.setter
    def biz_trace_id(self, value):
        self._biz_trace_id = value
    @property
    def invoice_amount_info(self):
        return self._invoice_amount_info

    @invoice_amount_info.setter
    def invoice_amount_info(self, value):
        if isinstance(value, InvoiceAmountInfo):
            self._invoice_amount_info = value
        else:
            self._invoice_amount_info = InvoiceAmountInfo.from_alipay_dict(value)
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseInvoiceBalanceQueryResponse, self).parse_response_content(response_content)
        if 'biz_trace_id' in response:
            self.biz_trace_id = response['biz_trace_id']
        if 'invoice_amount_info' in response:
            self.invoice_amount_info = response['invoice_amount_info']
        if 'message' in response:
            self.message = response['message']
