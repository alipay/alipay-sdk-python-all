#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.QueryInvoiceDetail import QueryInvoiceDetail


class AlipayCloudCloudbaseInvoiceDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseInvoiceDetailQueryResponse, self).__init__()
        self._biz_trace_id = None
        self._message = None
        self._query_invoice_details = None

    @property
    def biz_trace_id(self):
        return self._biz_trace_id

    @biz_trace_id.setter
    def biz_trace_id(self, value):
        self._biz_trace_id = value
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
    @property
    def query_invoice_details(self):
        return self._query_invoice_details

    @query_invoice_details.setter
    def query_invoice_details(self, value):
        if isinstance(value, list):
            self._query_invoice_details = list()
            for i in value:
                if isinstance(i, QueryInvoiceDetail):
                    self._query_invoice_details.append(i)
                else:
                    self._query_invoice_details.append(QueryInvoiceDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseInvoiceDetailQueryResponse, self).parse_response_content(response_content)
        if 'biz_trace_id' in response:
            self.biz_trace_id = response['biz_trace_id']
        if 'message' in response:
            self.message = response['message']
        if 'query_invoice_details' in response:
            self.query_invoice_details = response['query_invoice_details']
