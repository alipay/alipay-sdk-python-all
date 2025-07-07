#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PreInvoiceData import PreInvoiceData


class AlipayCloudCloudbaseInvoiceGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseInvoiceGetResponse, self).__init__()
        self._apply_id = None
        self._biz_trace_id = None
        self._invoice_datas = None
        self._message = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def biz_trace_id(self):
        return self._biz_trace_id

    @biz_trace_id.setter
    def biz_trace_id(self, value):
        self._biz_trace_id = value
    @property
    def invoice_datas(self):
        return self._invoice_datas

    @invoice_datas.setter
    def invoice_datas(self, value):
        if isinstance(value, list):
            self._invoice_datas = list()
            for i in value:
                if isinstance(i, PreInvoiceData):
                    self._invoice_datas.append(i)
                else:
                    self._invoice_datas.append(PreInvoiceData.from_alipay_dict(i))
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseInvoiceGetResponse, self).parse_response_content(response_content)
        if 'apply_id' in response:
            self.apply_id = response['apply_id']
        if 'biz_trace_id' in response:
            self.biz_trace_id = response['biz_trace_id']
        if 'invoice_datas' in response:
            self.invoice_datas = response['invoice_datas']
        if 'message' in response:
            self.message = response['message']
