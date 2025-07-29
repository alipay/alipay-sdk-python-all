#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskPolicyCaptchaCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskPolicyCaptchaCheckResponse, self).__init__()
        self._action = None
        self._captcha_config = None
        self._trace = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def captcha_config(self):
        return self._captcha_config

    @captcha_config.setter
    def captcha_config(self, value):
        self._captcha_config = value
    @property
    def trace(self):
        return self._trace

    @trace.setter
    def trace(self, value):
        self._trace = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskPolicyCaptchaCheckResponse, self).parse_response_content(response_content)
        if 'action' in response:
            self.action = response['action']
        if 'captcha_config' in response:
            self.captcha_config = response['captcha_config']
        if 'trace' in response:
            self.trace = response['trace']
