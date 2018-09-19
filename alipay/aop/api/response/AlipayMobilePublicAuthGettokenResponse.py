#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMobilePublicAuthGettokenResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMobilePublicAuthGettokenResponse, self).__init__()
        self._code = None
        self._msg = None
        self._token = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value
    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value

    def parse_response_content(self, response_content):
        response = super(AlipayMobilePublicAuthGettokenResponse, self).parse_response_content(response_content)
        if 'code' in response:
            self.code = response['code']
        if 'msg' in response:
            self.msg = response['msg']
        if 'token' in response:
            self.token = response['token']
