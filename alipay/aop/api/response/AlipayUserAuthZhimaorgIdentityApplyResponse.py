#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAuthZhimaorgIdentityApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAuthZhimaorgIdentityApplyResponse, self).__init__()
        self._access_token = None
        self._auth_token_type = None
        self._refresh_token = None

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value
    @property
    def auth_token_type(self):
        return self._auth_token_type

    @auth_token_type.setter
    def auth_token_type(self, value):
        self._auth_token_type = value
    @property
    def refresh_token(self):
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, value):
        self._refresh_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAuthZhimaorgIdentityApplyResponse, self).parse_response_content(response_content)
        if 'access_token' in response:
            self.access_token = response['access_token']
        if 'auth_token_type' in response:
            self.auth_token_type = response['auth_token_type']
        if 'refresh_token' in response:
            self.refresh_token = response['refresh_token']
