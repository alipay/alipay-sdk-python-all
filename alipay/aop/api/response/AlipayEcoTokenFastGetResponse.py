#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoTokenFastGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoTokenFastGetResponse, self).__init__()
        self._access_token = None
        self._expected_expires_in = None
        self._expires_in = None
        self._machine_code = None
        self._refresh_token = None

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value
    @property
    def expected_expires_in(self):
        return self._expected_expires_in

    @expected_expires_in.setter
    def expected_expires_in(self, value):
        self._expected_expires_in = value
    @property
    def expires_in(self):
        return self._expires_in

    @expires_in.setter
    def expires_in(self, value):
        self._expires_in = value
    @property
    def machine_code(self):
        return self._machine_code

    @machine_code.setter
    def machine_code(self, value):
        self._machine_code = value
    @property
    def refresh_token(self):
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, value):
        self._refresh_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoTokenFastGetResponse, self).parse_response_content(response_content)
        if 'access_token' in response:
            self.access_token = response['access_token']
        if 'expected_expires_in' in response:
            self.expected_expires_in = response['expected_expires_in']
        if 'expires_in' in response:
            self.expires_in = response['expires_in']
        if 'machine_code' in response:
            self.machine_code = response['machine_code']
        if 'refresh_token' in response:
            self.refresh_token = response['refresh_token']
