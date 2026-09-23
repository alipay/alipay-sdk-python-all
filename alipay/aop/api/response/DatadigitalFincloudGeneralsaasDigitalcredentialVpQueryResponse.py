#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalFincloudGeneralsaasDigitalcredentialVpQueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudGeneralsaasDigitalcredentialVpQueryResponse, self).__init__()
        self._cipher = None
        self._key_alias = None
        self._key_cipher = None

    @property
    def cipher(self):
        return self._cipher

    @cipher.setter
    def cipher(self, value):
        self._cipher = value
    @property
    def key_alias(self):
        return self._key_alias

    @key_alias.setter
    def key_alias(self, value):
        self._key_alias = value
    @property
    def key_cipher(self):
        return self._key_cipher

    @key_cipher.setter
    def key_cipher(self, value):
        self._key_cipher = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudGeneralsaasDigitalcredentialVpQueryResponse, self).parse_response_content(response_content)
        if 'cipher' in response:
            self.cipher = response['cipher']
        if 'key_alias' in response:
            self.key_alias = response['key_alias']
        if 'key_cipher' in response:
            self.key_cipher = response['key_cipher']
