#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceCognitiveOcrVehicleplateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCognitiveOcrVehicleplateQueryResponse, self).__init__()
        self._error_content = None
        self._prob = None
        self._request_id = None
        self._success = None
        self._trace_id = None
        self._txt = None

    @property
    def error_content(self):
        return self._error_content

    @error_content.setter
    def error_content(self, value):
        self._error_content = value
    @property
    def prob(self):
        return self._prob

    @prob.setter
    def prob(self, value):
        self._prob = value
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
    @property
    def txt(self):
        return self._txt

    @txt.setter
    def txt(self, value):
        self._txt = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCognitiveOcrVehicleplateQueryResponse, self).parse_response_content(response_content)
        if 'error_content' in response:
            self.error_content = response['error_content']
        if 'prob' in response:
            self.prob = response['prob']
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'success' in response:
            self.success = response['success']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
        if 'txt' in response:
            self.txt = response['txt']
