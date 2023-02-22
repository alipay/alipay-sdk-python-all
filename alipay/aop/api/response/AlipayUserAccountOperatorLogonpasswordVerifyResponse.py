#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAccountOperatorLogonpasswordVerifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAccountOperatorLogonpasswordVerifyResponse, self).__init__()
        self._fail_reason = None
        self._fail_times = None
        self._verify_success = None

    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def fail_times(self):
        return self._fail_times

    @fail_times.setter
    def fail_times(self, value):
        self._fail_times = value
    @property
    def verify_success(self):
        return self._verify_success

    @verify_success.setter
    def verify_success(self, value):
        self._verify_success = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAccountOperatorLogonpasswordVerifyResponse, self).parse_response_content(response_content)
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'fail_times' in response:
            self.fail_times = response['fail_times']
        if 'verify_success' in response:
            self.verify_success = response['verify_success']
