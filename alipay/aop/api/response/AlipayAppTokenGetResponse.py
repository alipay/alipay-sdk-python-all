#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAppTokenGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAppTokenGetResponse, self).__init__()
        self._app_access_token = None
        self._expires_in = None

    @property
    def app_access_token(self):
        return self._app_access_token

    @app_access_token.setter
    def app_access_token(self, value):
        self._app_access_token = value
    @property
    def expires_in(self):
        return self._expires_in

    @expires_in.setter
    def expires_in(self, value):
        self._expires_in = value

    def parse_response_content(self, response_content):
        response = super(AlipayAppTokenGetResponse, self).parse_response_content(response_content)
        if 'app_access_token' in response:
            self.app_access_token = response['app_access_token']
        if 'expires_in' in response:
            self.expires_in = response['expires_in']
