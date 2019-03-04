#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPeUserAuthApplyResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeUserAuthApplyResponse, self).__init__()
        self._auth_code = None
        self._error_scope = None
        self._scope = None
        self._state = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def error_scope(self):
        return self._error_scope

    @error_scope.setter
    def error_scope(self, value):
        self._error_scope = value
    @property
    def scope(self):
        return self._scope

    @scope.setter
    def scope(self, value):
        self._scope = value
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeUserAuthApplyResponse, self).parse_response_content(response_content)
        if 'auth_code' in response:
            self.auth_code = response['auth_code']
        if 'error_scope' in response:
            self.error_scope = response['error_scope']
        if 'scope' in response:
            self.scope = response['scope']
        if 'state' in response:
            self.state = response['state']
