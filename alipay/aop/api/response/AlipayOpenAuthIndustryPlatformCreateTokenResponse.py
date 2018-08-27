#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAuthIndustryPlatformCreateTokenResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAuthIndustryPlatformCreateTokenResponse, self).__init__()
        self._auth_code = None
        self._requst_app_id = None
        self._scope = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def requst_app_id(self):
        return self._requst_app_id

    @requst_app_id.setter
    def requst_app_id(self, value):
        self._requst_app_id = value
    @property
    def scope(self):
        return self._scope

    @scope.setter
    def scope(self, value):
        self._scope = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAuthIndustryPlatformCreateTokenResponse, self).parse_response_content(response_content)
        if 'auth_code' in response:
            self.auth_code = response['auth_code']
        if 'requst_app_id' in response:
            self.requst_app_id = response['requst_app_id']
        if 'scope' in response:
            self.scope = response['scope']
