#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneCommonPremissionAuthResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneCommonPremissionAuthResponse, self).__init__()
        self._auth_code = None
        self._expiration = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def expiration(self):
        return self._expiration

    @expiration.setter
    def expiration(self, value):
        self._expiration = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneCommonPremissionAuthResponse, self).parse_response_content(response_content)
        if 'auth_code' in response:
            self.auth_code = response['auth_code']
        if 'expiration' in response:
            self.expiration = response['expiration']
