#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditSceneprodVidGetResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSceneprodVidGetResponse, self).__init__()
        self._retry = None
        self._trace_id = None
        self._verify_id = None

    @property
    def retry(self):
        return self._retry

    @retry.setter
    def retry(self, value):
        self._retry = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value
    @property
    def verify_id(self):
        return self._verify_id

    @verify_id.setter
    def verify_id(self, value):
        self._verify_id = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSceneprodVidGetResponse, self).parse_response_content(response_content)
        if 'retry' in response:
            self.retry = response['retry']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
        if 'verify_id' in response:
            self.verify_id = response['verify_id']
