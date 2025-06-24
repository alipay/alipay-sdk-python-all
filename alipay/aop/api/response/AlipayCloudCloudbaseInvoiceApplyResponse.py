#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseInvoiceApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseInvoiceApplyResponse, self).__init__()
        self._apply_id = None
        self._biz_trace_id = None
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
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseInvoiceApplyResponse, self).parse_response_content(response_content)
        if 'apply_id' in response:
            self.apply_id = response['apply_id']
        if 'biz_trace_id' in response:
            self.biz_trace_id = response['biz_trace_id']
        if 'message' in response:
            self.message = response['message']
