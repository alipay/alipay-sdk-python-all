#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalFincloudGeneralsaasFaceCertifyCertifyResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudGeneralsaasFaceCertifyCertifyResponse, self).__init__()
        self._extern_info = None
        self._mismatch_reason = None
        self._passed = None

    @property
    def extern_info(self):
        return self._extern_info

    @extern_info.setter
    def extern_info(self, value):
        self._extern_info = value
    @property
    def mismatch_reason(self):
        return self._mismatch_reason

    @mismatch_reason.setter
    def mismatch_reason(self, value):
        self._mismatch_reason = value
    @property
    def passed(self):
        return self._passed

    @passed.setter
    def passed(self, value):
        self._passed = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudGeneralsaasFaceCertifyCertifyResponse, self).parse_response_content(response_content)
        if 'extern_info' in response:
            self.extern_info = response['extern_info']
        if 'mismatch_reason' in response:
            self.mismatch_reason = response['mismatch_reason']
        if 'passed' in response:
            self.passed = response['passed']
