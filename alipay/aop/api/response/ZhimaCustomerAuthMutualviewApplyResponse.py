#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCustomerAuthMutualviewApplyResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerAuthMutualviewApplyResponse, self).__init__()
        self._auth_id = None
        self._cancel_result = None
        self._describe = None
        self._error_code = None
        self._error_message = None
        self._outer_sign = None

    @property
    def auth_id(self):
        return self._auth_id

    @auth_id.setter
    def auth_id(self, value):
        self._auth_id = value
    @property
    def cancel_result(self):
        return self._cancel_result

    @cancel_result.setter
    def cancel_result(self, value):
        self._cancel_result = value
    @property
    def describe(self):
        return self._describe

    @describe.setter
    def describe(self, value):
        self._describe = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        self._error_message = value
    @property
    def outer_sign(self):
        return self._outer_sign

    @outer_sign.setter
    def outer_sign(self, value):
        self._outer_sign = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCustomerAuthMutualviewApplyResponse, self).parse_response_content(response_content)
        if 'auth_id' in response:
            self.auth_id = response['auth_id']
        if 'cancel_result' in response:
            self.cancel_result = response['cancel_result']
        if 'describe' in response:
            self.describe = response['describe']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_message' in response:
            self.error_message = response['error_message']
        if 'outer_sign' in response:
            self.outer_sign = response['outer_sign']
