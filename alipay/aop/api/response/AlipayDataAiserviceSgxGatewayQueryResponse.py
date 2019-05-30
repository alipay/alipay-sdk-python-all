#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataAiserviceSgxGatewayQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataAiserviceSgxGatewayQueryResponse, self).__init__()
        self._request_uuid = None
        self._result = None

    @property
    def request_uuid(self):
        return self._request_uuid

    @request_uuid.setter
    def request_uuid(self, value):
        self._request_uuid = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataAiserviceSgxGatewayQueryResponse, self).parse_response_content(response_content)
        if 'request_uuid' in response:
            self.request_uuid = response['request_uuid']
        if 'result' in response:
            self.result = response['result']
