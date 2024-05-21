#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpFinRiskIdentifyResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpFinRiskIdentifyResponse, self).__init__()
        self._request_id = None
        self._result = None

    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpFinRiskIdentifyResponse, self).parse_response_content(response_content)
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'result' in response:
            self.result = response['result']
