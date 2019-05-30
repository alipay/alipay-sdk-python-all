#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenStsTokenGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenStsTokenGetResponse, self).__init__()
        self._expiration = None
        self._security_token = None

    @property
    def expiration(self):
        return self._expiration

    @expiration.setter
    def expiration(self, value):
        self._expiration = value
    @property
    def security_token(self):
        return self._security_token

    @security_token.setter
    def security_token(self, value):
        self._security_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenStsTokenGetResponse, self).parse_response_content(response_content)
        if 'expiration' in response:
            self.expiration = response['expiration']
        if 'security_token' in response:
            self.security_token = response['security_token']
