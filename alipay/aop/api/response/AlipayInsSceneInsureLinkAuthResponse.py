#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneInsureLinkAuthResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneInsureLinkAuthResponse, self).__init__()
        self._authed_token = None
        self._expiration = None
        self._insure_url = None

    @property
    def authed_token(self):
        return self._authed_token

    @authed_token.setter
    def authed_token(self, value):
        self._authed_token = value
    @property
    def expiration(self):
        return self._expiration

    @expiration.setter
    def expiration(self, value):
        self._expiration = value
    @property
    def insure_url(self):
        return self._insure_url

    @insure_url.setter
    def insure_url(self, value):
        self._insure_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneInsureLinkAuthResponse, self).parse_response_content(response_content)
        if 'authed_token' in response:
            self.authed_token = response['authed_token']
        if 'expiration' in response:
            self.expiration = response['expiration']
        if 'insure_url' in response:
            self.insure_url = response['insure_url']
