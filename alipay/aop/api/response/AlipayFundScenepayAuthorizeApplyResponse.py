#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundScenepayAuthorizeApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundScenepayAuthorizeApplyResponse, self).__init__()
        self._apply_token = None
        self._apply_url = None

    @property
    def apply_token(self):
        return self._apply_token

    @apply_token.setter
    def apply_token(self, value):
        self._apply_token = value
    @property
    def apply_url(self):
        return self._apply_url

    @apply_url.setter
    def apply_url(self, value):
        self._apply_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundScenepayAuthorizeApplyResponse, self).parse_response_content(response_content)
        if 'apply_token' in response:
            self.apply_token = response['apply_token']
        if 'apply_url' in response:
            self.apply_url = response['apply_url']
