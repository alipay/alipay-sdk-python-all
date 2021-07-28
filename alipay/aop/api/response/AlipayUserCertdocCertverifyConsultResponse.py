#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserCertdocCertverifyConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserCertdocCertverifyConsultResponse, self).__init__()
        self._fail_params = None
        self._fail_reason = None
        self._passed = None

    @property
    def fail_params(self):
        return self._fail_params

    @fail_params.setter
    def fail_params(self, value):
        self._fail_params = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def passed(self):
        return self._passed

    @passed.setter
    def passed(self, value):
        self._passed = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserCertdocCertverifyConsultResponse, self).parse_response_content(response_content)
        if 'fail_params' in response:
            self.fail_params = response['fail_params']
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'passed' in response:
            self.passed = response['passed']
