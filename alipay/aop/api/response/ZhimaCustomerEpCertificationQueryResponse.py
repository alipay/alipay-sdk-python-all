#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCustomerEpCertificationQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerEpCertificationQueryResponse, self).__init__()
        self._failed_reason = None
        self._passed = None

    @property
    def failed_reason(self):
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, value):
        self._failed_reason = value
    @property
    def passed(self):
        return self._passed

    @passed.setter
    def passed(self, value):
        self._passed = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCustomerEpCertificationQueryResponse, self).parse_response_content(response_content)
        if 'failed_reason' in response:
            self.failed_reason = response['failed_reason']
        if 'passed' in response:
            self.passed = response['passed']
