#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskVerifyidentityInitializeResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskVerifyidentityInitializeResponse, self).__init__()
        self._biz_data = None
        self._err_msg = None
        self._error_code = None
        self._is_success = None
        self._verify_url = None
        self._veritfy_token = None

    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def err_msg(self):
        return self._err_msg

    @err_msg.setter
    def err_msg(self, value):
        self._err_msg = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def is_success(self):
        return self._is_success

    @is_success.setter
    def is_success(self, value):
        self._is_success = value
    @property
    def verify_url(self):
        return self._verify_url

    @verify_url.setter
    def verify_url(self, value):
        self._verify_url = value
    @property
    def veritfy_token(self):
        return self._veritfy_token

    @veritfy_token.setter
    def veritfy_token(self, value):
        self._veritfy_token = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskVerifyidentityInitializeResponse, self).parse_response_content(response_content)
        if 'biz_data' in response:
            self.biz_data = response['biz_data']
        if 'err_msg' in response:
            self.err_msg = response['err_msg']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'is_success' in response:
            self.is_success = response['is_success']
        if 'verify_url' in response:
            self.verify_url = response['verify_url']
        if 'veritfy_token' in response:
            self.veritfy_token = response['veritfy_token']
