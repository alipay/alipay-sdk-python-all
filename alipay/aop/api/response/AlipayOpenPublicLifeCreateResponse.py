#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicLifeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicLifeCreateResponse, self).__init__()
        self._expire_time = None
        self._public_id = None
        self._public_long_link = None
        self._public_short_link = None
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
    def public_long_link(self):
        return self._public_long_link

    @public_long_link.setter
    def public_long_link(self, value):
        self._public_long_link = value
    @property
    def public_short_link(self):
        return self._public_short_link

    @public_short_link.setter
    def public_short_link(self, value):
        self._public_short_link = value
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
        response = super(AlipayOpenPublicLifeCreateResponse, self).parse_response_content(response_content)
        if 'expire_time' in response:
            self.expire_time = response['expire_time']
        if 'public_id' in response:
            self.public_id = response['public_id']
        if 'public_long_link' in response:
            self.public_long_link = response['public_long_link']
        if 'public_short_link' in response:
            self.public_short_link = response['public_short_link']
        if 'refresh_token' in response:
            self.refresh_token = response['refresh_token']
        if 'token' in response:
            self.token = response['token']
