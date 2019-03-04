#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAuthAppApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAuthAppApplyResponse, self).__init__()
        self._app_auth_token = None
        self._app_refresh_token = None

    @property
    def app_auth_token(self):
        return self._app_auth_token

    @app_auth_token.setter
    def app_auth_token(self, value):
        self._app_auth_token = value
    @property
    def app_refresh_token(self):
        return self._app_refresh_token

    @app_refresh_token.setter
    def app_refresh_token(self, value):
        self._app_refresh_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAuthAppApplyResponse, self).parse_response_content(response_content)
        if 'app_auth_token' in response:
            self.app_auth_token = response['app_auth_token']
        if 'app_refresh_token' in response:
            self.app_refresh_token = response['app_refresh_token']
