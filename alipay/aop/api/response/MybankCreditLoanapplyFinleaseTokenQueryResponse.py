#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditLoanapplyFinleaseTokenQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoanapplyFinleaseTokenQueryResponse, self).__init__()
        self._reason = None
        self._security_url = None
        self._valid = None

    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def security_url(self):
        return self._security_url

    @security_url.setter
    def security_url(self, value):
        self._security_url = value
    @property
    def valid(self):
        return self._valid

    @valid.setter
    def valid(self, value):
        self._valid = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoanapplyFinleaseTokenQueryResponse, self).parse_response_content(response_content)
        if 'reason' in response:
            self.reason = response['reason']
        if 'security_url' in response:
            self.security_url = response['security_url']
        if 'valid' in response:
            self.valid = response['valid']
