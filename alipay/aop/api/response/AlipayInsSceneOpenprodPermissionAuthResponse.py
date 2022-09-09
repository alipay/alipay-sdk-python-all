#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneOpenprodPermissionAuthResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneOpenprodPermissionAuthResponse, self).__init__()
        self._auth_token = None
        self._expiration = None

    @property
    def auth_token(self):
        return self._auth_token

    @auth_token.setter
    def auth_token(self, value):
        self._auth_token = value
    @property
    def expiration(self):
        return self._expiration

    @expiration.setter
    def expiration(self, value):
        self._expiration = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneOpenprodPermissionAuthResponse, self).parse_response_content(response_content)
        if 'auth_token' in response:
            self.auth_token = response['auth_token']
        if 'expiration' in response:
            self.expiration = response['expiration']
