#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechNftOauthtokenApplyResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftOauthtokenApplyResponse, self).__init__()
        self._access_token = None
        self._expire_time = None
        self._open_user_id = None
        self._refresh_expire_time = None
        self._refresh_token = None
        self._req_msg_id = None

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def open_user_id(self):
        return self._open_user_id

    @open_user_id.setter
    def open_user_id(self, value):
        self._open_user_id = value
    @property
    def refresh_expire_time(self):
        return self._refresh_expire_time

    @refresh_expire_time.setter
    def refresh_expire_time(self, value):
        self._refresh_expire_time = value
    @property
    def refresh_token(self):
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, value):
        self._refresh_token = value
    @property
    def req_msg_id(self):
        return self._req_msg_id

    @req_msg_id.setter
    def req_msg_id(self, value):
        self._req_msg_id = value

    def parse_response_content(self, response_content):
        response = super(AnttechNftOauthtokenApplyResponse, self).parse_response_content(response_content)
        if 'access_token' in response:
            self.access_token = response['access_token']
        if 'expire_time' in response:
            self.expire_time = response['expire_time']
        if 'open_user_id' in response:
            self.open_user_id = response['open_user_id']
        if 'refresh_expire_time' in response:
            self.refresh_expire_time = response['refresh_expire_time']
        if 'refresh_token' in response:
            self.refresh_token = response['refresh_token']
        if 'req_msg_id' in response:
            self.req_msg_id = response['req_msg_id']
