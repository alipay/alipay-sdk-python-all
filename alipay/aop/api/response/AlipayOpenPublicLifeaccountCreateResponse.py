#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicLifeAccountCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicLifeAccountCreateResponse, self).__init__()
        self._expire_time = None
        self._public_id = None
        self._refresh_token = None
        self._token = None

    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def public_id(self):
        return self._public_id

    @public_id.setter
    def public_id(self, value):
        self._public_id = value
    @property
    def refresh_token(self):
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, value):
        self._refresh_token = value
    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicLifeAccountCreateResponse, self).parse_response_content(response_content)
        if 'expire_time' in response:
            self.expire_time = response['expire_time']
        if 'public_id' in response:
            self.public_id = response['public_id']
        if 'refresh_token' in response:
            self.refresh_token = response['refresh_token']
        if 'token' in response:
            self.token = response['token']
