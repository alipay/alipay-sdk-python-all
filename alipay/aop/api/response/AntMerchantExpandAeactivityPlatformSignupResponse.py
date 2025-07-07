#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandAeactivityPlatformSignupResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandAeactivityPlatformSignupResponse, self).__init__()
        self._signup_result = None

    @property
    def signup_result(self):
        return self._signup_result

    @signup_result.setter
    def signup_result(self, value):
        self._signup_result = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandAeactivityPlatformSignupResponse, self).parse_response_content(response_content)
        if 'signup_result' in response:
            self.signup_result = response['signup_result']
