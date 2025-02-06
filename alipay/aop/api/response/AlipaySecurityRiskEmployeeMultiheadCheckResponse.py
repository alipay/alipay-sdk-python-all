#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskEmployeeMultiheadCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskEmployeeMultiheadCheckResponse, self).__init__()
        self._accept_no = None
        self._request_no = None

    @property
    def accept_no(self):
        return self._accept_no

    @accept_no.setter
    def accept_no(self, value):
        self._accept_no = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskEmployeeMultiheadCheckResponse, self).parse_response_content(response_content)
        if 'accept_no' in response:
            self.accept_no = response['accept_no']
        if 'request_no' in response:
            self.request_no = response['request_no']
