#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundEnterprisepaySignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundEnterprisepaySignResponse, self).__init__()
        self._sign_token = None
        self._sign_url = None

    @property
    def sign_token(self):
        return self._sign_token

    @sign_token.setter
    def sign_token(self, value):
        self._sign_token = value
    @property
    def sign_url(self):
        return self._sign_url

    @sign_url.setter
    def sign_url(self, value):
        self._sign_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundEnterprisepaySignResponse, self).parse_response_content(response_content)
        if 'sign_token' in response:
            self.sign_token = response['sign_token']
        if 'sign_url' in response:
            self.sign_url = response['sign_url']
