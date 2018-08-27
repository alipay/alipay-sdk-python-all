#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppAuthsubsAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppAuthsubsAddResponse, self).__init__()
        self._auth_code = None
        self._invalid_date = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def invalid_date(self):
        return self._invalid_date

    @invalid_date.setter
    def invalid_date(self, value):
        self._invalid_date = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppAuthsubsAddResponse, self).parse_response_content(response_content)
        if 'auth_code' in response:
            self.auth_code = response['auth_code']
        if 'invalid_date' in response:
            self.invalid_date = response['invalid_date']
