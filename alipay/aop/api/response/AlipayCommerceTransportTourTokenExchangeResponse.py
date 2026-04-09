#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportTourTokenExchangeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportTourTokenExchangeResponse, self).__init__()
        self._auth_code = None
        self._code_type = None
        self._expire_date = None
        self._start_date = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def code_type(self):
        return self._code_type

    @code_type.setter
    def code_type(self, value):
        self._code_type = value
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportTourTokenExchangeResponse, self).parse_response_content(response_content)
        if 'auth_code' in response:
            self.auth_code = response['auth_code']
        if 'code_type' in response:
            self.code_type = response['code_type']
        if 'expire_date' in response:
            self.expire_date = response['expire_date']
        if 'start_date' in response:
            self.start_date = response['start_date']
