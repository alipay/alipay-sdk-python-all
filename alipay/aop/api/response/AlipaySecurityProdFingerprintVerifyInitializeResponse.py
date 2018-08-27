#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdFingerprintVerifyInitializeResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdFingerprintVerifyInitializeResponse, self).__init__()
        self._server_response = None

    @property
    def server_response(self):
        return self._server_response

    @server_response.setter
    def server_response(self, value):
        self._server_response = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdFingerprintVerifyInitializeResponse, self).parse_response_content(response_content)
        if 'server_response' in response:
            self.server_response = response['server_response']
