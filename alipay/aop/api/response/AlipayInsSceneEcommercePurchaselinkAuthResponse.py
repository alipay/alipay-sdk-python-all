#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneEcommercePurchaselinkAuthResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneEcommercePurchaselinkAuthResponse, self).__init__()
        self._authed_token = None
        self._authed_url = None
        self._expiration = None

    @property
    def authed_token(self):
        return self._authed_token

    @authed_token.setter
    def authed_token(self, value):
        self._authed_token = value
    @property
    def authed_url(self):
        return self._authed_url

    @authed_url.setter
    def authed_url(self, value):
        self._authed_url = value
    @property
    def expiration(self):
        return self._expiration

    @expiration.setter
    def expiration(self, value):
        self._expiration = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneEcommercePurchaselinkAuthResponse, self).parse_response_content(response_content)
        if 'authed_token' in response:
            self.authed_token = response['authed_token']
        if 'authed_url' in response:
            self.authed_url = response['authed_url']
        if 'expiration' in response:
            self.expiration = response['expiration']
