#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdFingerprintApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdFingerprintApplyResponse, self).__init__()
        self._auth_type = None
        self._device_id = None
        self._token = None

    @property
    def auth_type(self):
        return self._auth_type

    @auth_type.setter
    def auth_type(self, value):
        self._auth_type = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdFingerprintApplyResponse, self).parse_response_content(response_content)
        if 'auth_type' in response:
            self.auth_type = response['auth_type']
        if 'device_id' in response:
            self.device_id = response['device_id']
        if 'token' in response:
            self.token = response['token']
