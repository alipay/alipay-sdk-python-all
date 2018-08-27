#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskPolicyConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskPolicyConfirmResponse, self).__init__()
        self._confirm_success = None
        self._success = None

    @property
    def confirm_success(self):
        return self._confirm_success

    @confirm_success.setter
    def confirm_success(self, value):
        self._confirm_success = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskPolicyConfirmResponse, self).parse_response_content(response_content)
        if 'confirm_success' in response:
            self.confirm_success = response['confirm_success']
        if 'success' in response:
            self.success = response['success']
