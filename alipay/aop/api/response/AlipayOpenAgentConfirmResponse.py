#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAgentConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAgentConfirmResponse, self).__init__()
        self._app_auth_token = None
        self._app_refresh_token = None
        self._auth_app_id = None
        self._expires_in = None
        self._re_expires_in = None
        self._user_id = None

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
    @property
    def auth_app_id(self):
        return self._auth_app_id

    @auth_app_id.setter
    def auth_app_id(self, value):
        self._auth_app_id = value
    @property
    def expires_in(self):
        return self._expires_in

    @expires_in.setter
    def expires_in(self, value):
        self._expires_in = value
    @property
    def re_expires_in(self):
        return self._re_expires_in

    @re_expires_in.setter
    def re_expires_in(self, value):
        self._re_expires_in = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAgentConfirmResponse, self).parse_response_content(response_content)
        if 'app_auth_token' in response:
            self.app_auth_token = response['app_auth_token']
        if 'app_refresh_token' in response:
            self.app_refresh_token = response['app_refresh_token']
        if 'auth_app_id' in response:
            self.auth_app_id = response['auth_app_id']
        if 'expires_in' in response:
            self.expires_in = response['expires_in']
        if 're_expires_in' in response:
            self.re_expires_in = response['re_expires_in']
        if 'user_id' in response:
            self.user_id = response['user_id']
