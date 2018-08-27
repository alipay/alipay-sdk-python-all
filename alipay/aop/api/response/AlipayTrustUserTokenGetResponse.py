#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTrustUserTokenGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTrustUserTokenGetResponse, self).__init__()
        self._access_token = None
        self._refresh_token = None

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value
    @property
    def refresh_token(self):
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, value):
        self._refresh_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayTrustUserTokenGetResponse, self).parse_response_content(response_content)
        if 'access_token' in response:
            self.access_token = response['access_token']
        if 'refresh_token' in response:
            self.refresh_token = response['refresh_token']
