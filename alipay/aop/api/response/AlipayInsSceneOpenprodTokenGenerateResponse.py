#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneOpenprodTokenGenerateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneOpenprodTokenGenerateResponse, self).__init__()
        self._expiration = None
        self._identity_token = None

    @property
    def expiration(self):
        return self._expiration

    @expiration.setter
    def expiration(self, value):
        self._expiration = value
    @property
    def identity_token(self):
        return self._identity_token

    @identity_token.setter
    def identity_token(self, value):
        self._identity_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneOpenprodTokenGenerateResponse, self).parse_response_content(response_content)
        if 'expiration' in response:
            self.expiration = response['expiration']
        if 'identity_token' in response:
            self.identity_token = response['identity_token']
