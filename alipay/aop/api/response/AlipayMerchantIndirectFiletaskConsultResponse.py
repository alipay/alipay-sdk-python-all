#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantIndirectFiletaskConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantIndirectFiletaskConsultResponse, self).__init__()
        self._auth_token = None
        self._file_url = None
        self._result_code = None

    @property
    def auth_token(self):
        return self._auth_token

    @auth_token.setter
    def auth_token(self, value):
        self._auth_token = value
    @property
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantIndirectFiletaskConsultResponse, self).parse_response_content(response_content)
        if 'auth_token' in response:
            self.auth_token = response['auth_token']
        if 'file_url' in response:
            self.file_url = response['file_url']
        if 'result_code' in response:
            self.result_code = response['result_code']
