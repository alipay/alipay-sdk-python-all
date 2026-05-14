#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdSecdeviceInitializeResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdSecdeviceInitializeResponse, self).__init__()
        self._ifaa_token = None
        self._server_response = None

    @property
    def ifaa_token(self):
        return self._ifaa_token

    @ifaa_token.setter
    def ifaa_token(self, value):
        self._ifaa_token = value
    @property
    def server_response(self):
        return self._server_response

    @server_response.setter
    def server_response(self, value):
        self._server_response = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdSecdeviceInitializeResponse, self).parse_response_content(response_content)
        if 'ifaa_token' in response:
            self.ifaa_token = response['ifaa_token']
        if 'server_response' in response:
            self.server_response = response['server_response']
