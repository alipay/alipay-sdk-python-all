#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditSupplychainCreditpaySellerunsignCreateResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSupplychainCreditpaySellerunsignCreateResponse, self).__init__()
        self._fail_reason = None
        self._retry = None
        self._trace_id = None
        self._unsign_result = None

    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
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
    def unsign_result(self):
        return self._unsign_result

    @unsign_result.setter
    def unsign_result(self, value):
        self._unsign_result = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSupplychainCreditpaySellerunsignCreateResponse, self).parse_response_content(response_content)
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'retry' in response:
            self.retry = response['retry']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
        if 'unsign_result' in response:
            self.unsign_result = response['unsign_result']
