#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAuthUserinfoApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAuthUserinfoApplyResponse, self).__init__()
        self._auth_code = None
        self._user_id = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAuthUserinfoApplyResponse, self).parse_response_content(response_content)
        if 'auth_code' in response:
            self.auth_code = response['auth_code']
        if 'user_id' in response:
            self.user_id = response['user_id']
