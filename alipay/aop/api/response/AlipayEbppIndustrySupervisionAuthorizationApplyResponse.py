#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustrySupervisionAuthorizationApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustrySupervisionAuthorizationApplyResponse, self).__init__()
        self._apply_request_no = None
        self._sign_url = None

    @property
    def apply_request_no(self):
        return self._apply_request_no

    @apply_request_no.setter
    def apply_request_no(self, value):
        self._apply_request_no = value
    @property
    def sign_url(self):
        return self._sign_url

    @sign_url.setter
    def sign_url(self, value):
        self._sign_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustrySupervisionAuthorizationApplyResponse, self).parse_response_content(response_content)
        if 'apply_request_no' in response:
            self.apply_request_no = response['apply_request_no']
        if 'sign_url' in response:
            self.sign_url = response['sign_url']
