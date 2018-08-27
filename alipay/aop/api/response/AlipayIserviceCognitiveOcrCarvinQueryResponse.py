#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceCognitiveOcrCarvinQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCognitiveOcrCarvinQueryResponse, self).__init__()
        self._request_id = None
        self._trace_id = None
        self._vin = None

    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value
    @property
    def vin(self):
        return self._vin

    @vin.setter
    def vin(self, value):
        self._vin = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCognitiveOcrCarvinQueryResponse, self).parse_response_content(response_content)
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
        if 'vin' in response:
            self.vin = response['vin']
