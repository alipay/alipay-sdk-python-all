#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalAqTokenCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalAqTokenCreateResponse, self).__init__()
        self._access_token = None
        self._auth_start = None
        self._expires_in = None
        self._refresh_token = None

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value
    @property
    def auth_start(self):
        return self._auth_start

    @auth_start.setter
    def auth_start(self, value):
        self._auth_start = value
    @property
    def expires_in(self):
        return self._expires_in

    @expires_in.setter
    def expires_in(self, value):
        self._expires_in = value
    @property
    def refresh_token(self):
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, value):
        self._refresh_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalAqTokenCreateResponse, self).parse_response_content(response_content)
        if 'access_token' in response:
            self.access_token = response['access_token']
        if 'auth_start' in response:
            self.auth_start = response['auth_start']
        if 'expires_in' in response:
            self.expires_in = response['expires_in']
        if 'refresh_token' in response:
            self.refresh_token = response['refresh_token']
