#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditSceneprodLoanModifyResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSceneprodLoanModifyResponse, self).__init__()
        self._result_content = None
        self._retry = None
        self._trace_id = None

    @property
    def result_content(self):
        return self._result_content

    @result_content.setter
    def result_content(self, value):
        self._result_content = value
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

    def parse_response_content(self, response_content):
        response = super(MybankCreditSceneprodLoanModifyResponse, self).parse_response_content(response_content)
        if 'result_content' in response:
            self.result_content = response['result_content']
        if 'retry' in response:
            self.retry = response['retry']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
