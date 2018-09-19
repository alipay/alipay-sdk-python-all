#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceCognitiveOcrBankcardQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCognitiveOcrBankcardQueryResponse, self).__init__()
        self._card_num = None
        self._request_id = None
        self._success = None
        self._trace_id = None

    @property
    def card_num(self):
        return self._card_num

    @card_num.setter
    def card_num(self, value):
        self._card_num = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCognitiveOcrBankcardQueryResponse, self).parse_response_content(response_content)
        if 'card_num' in response:
            self.card_num = response['card_num']
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'success' in response:
            self.success = response['success']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
