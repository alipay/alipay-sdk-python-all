#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalFincloudGeneralsaasFaceSourceCertifyResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudGeneralsaasFaceSourceCertifyResponse, self).__init__()
        self._certify_no = None
        self._passed = None

    @property
    def certify_no(self):
        return self._certify_no

    @certify_no.setter
    def certify_no(self, value):
        self._certify_no = value
    @property
    def passed(self):
        return self._passed

    @passed.setter
    def passed(self, value):
        self._passed = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudGeneralsaasFaceSourceCertifyResponse, self).parse_response_content(response_content)
        if 'certify_no' in response:
            self.certify_no = response['certify_no']
        if 'passed' in response:
            self.passed = response['passed']
