#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAuthTokenAppQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAuthTokenAppQueryResponse, self).__init__()
        self._auth_app_id = None
        self._auth_end = None
        self._auth_methods = None
        self._auth_start = None
        self._expires_in = None
        self._status = None
        self._user_id = None

    @property
    def auth_app_id(self):
        return self._auth_app_id

    @auth_app_id.setter
    def auth_app_id(self, value):
        self._auth_app_id = value
    @property
    def auth_end(self):
        return self._auth_end

    @auth_end.setter
    def auth_end(self, value):
        self._auth_end = value
    @property
    def auth_methods(self):
        return self._auth_methods

    @auth_methods.setter
    def auth_methods(self, value):
        if isinstance(value, list):
            self._auth_methods = list()
            for i in value:
                self._auth_methods.append(i)
    @property
    def auth_start(self):
        return self._auth_start

    @auth_start.setter
    def auth_start(self, value):
        self._auth_start = value
    @property
    def expires_in(self):
        return self._expires_in

    @expires_in.setter
    def expires_in(self, value):
        self._expires_in = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAuthTokenAppQueryResponse, self).parse_response_content(response_content)
        if 'auth_app_id' in response:
            self.auth_app_id = response['auth_app_id']
        if 'auth_end' in response:
            self.auth_end = response['auth_end']
        if 'auth_methods' in response:
            self.auth_methods = response['auth_methods']
        if 'auth_start' in response:
            self.auth_start = response['auth_start']
        if 'expires_in' in response:
            self.expires_in = response['expires_in']
        if 'status' in response:
            self.status = response['status']
        if 'user_id' in response:
            self.user_id = response['user_id']
