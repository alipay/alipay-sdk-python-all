#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoTrafficCodeVerifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoTrafficCodeVerifyResponse, self).__init__()
        self._decode_success = None
        self._error_code = None
        self._error_msg = None
        self._parse_mode = None
        self._result_desc = None
        self._success = None
        self._verify_success = None

    @property
    def decode_success(self):
        return self._decode_success

    @decode_success.setter
    def decode_success(self, value):
        self._decode_success = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def parse_mode(self):
        return self._parse_mode

    @parse_mode.setter
    def parse_mode(self, value):
        self._parse_mode = value
    @property
    def result_desc(self):
        return self._result_desc

    @result_desc.setter
    def result_desc(self, value):
        self._result_desc = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
    @property
    def verify_success(self):
        return self._verify_success

    @verify_success.setter
    def verify_success(self, value):
        self._verify_success = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoTrafficCodeVerifyResponse, self).parse_response_content(response_content)
        if 'decode_success' in response:
            self.decode_success = response['decode_success']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_msg' in response:
            self.error_msg = response['error_msg']
        if 'parse_mode' in response:
            self.parse_mode = response['parse_mode']
        if 'result_desc' in response:
            self.result_desc = response['result_desc']
        if 'success' in response:
            self.success = response['success']
        if 'verify_success' in response:
            self.verify_success = response['verify_success']
