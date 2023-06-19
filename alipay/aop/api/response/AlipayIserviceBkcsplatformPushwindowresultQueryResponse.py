#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceBkcsplatformPushwindowresultQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceBkcsplatformPushwindowresultQueryResponse, self).__init__()
        self._feedback_values = None
        self._request_id = None
        self._request_token = None

    @property
    def feedback_values(self):
        return self._feedback_values

    @feedback_values.setter
    def feedback_values(self, value):
        self._feedback_values = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def request_token(self):
        return self._request_token

    @request_token.setter
    def request_token(self, value):
        self._request_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceBkcsplatformPushwindowresultQueryResponse, self).parse_response_content(response_content)
        if 'feedback_values' in response:
            self.feedback_values = response['feedback_values']
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'request_token' in response:
            self.request_token = response['request_token']
