#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCustomerCreditinfoSignResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerCreditinfoSignResponse, self).__init__()
        self._auth_result = None
        self._can_auth = None
        self._sign_id = None

    @property
    def auth_result(self):
        return self._auth_result

    @auth_result.setter
    def auth_result(self, value):
        self._auth_result = value
    @property
    def can_auth(self):
        return self._can_auth

    @can_auth.setter
    def can_auth(self, value):
        self._can_auth = value
    @property
    def sign_id(self):
        return self._sign_id

    @sign_id.setter
    def sign_id(self, value):
        self._sign_id = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCustomerCreditinfoSignResponse, self).parse_response_content(response_content)
        if 'auth_result' in response:
            self.auth_result = response['auth_result']
        if 'can_auth' in response:
            self.can_auth = response['can_auth']
        if 'sign_id' in response:
            self.sign_id = response['sign_id']
