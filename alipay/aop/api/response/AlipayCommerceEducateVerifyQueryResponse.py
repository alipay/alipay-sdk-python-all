#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateVerifyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateVerifyQueryResponse, self).__init__()
        self._open_id = None
        self._user_id = None
        self._verify_request_id = None
        self._verify_status = None
        self._verify_type = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def verify_request_id(self):
        return self._verify_request_id

    @verify_request_id.setter
    def verify_request_id(self, value):
        self._verify_request_id = value
    @property
    def verify_status(self):
        return self._verify_status

    @verify_status.setter
    def verify_status(self, value):
        self._verify_status = value
    @property
    def verify_type(self):
        return self._verify_type

    @verify_type.setter
    def verify_type(self, value):
        self._verify_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateVerifyQueryResponse, self).parse_response_content(response_content)
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'verify_request_id' in response:
            self.verify_request_id = response['verify_request_id']
        if 'verify_status' in response:
            self.verify_status = response['verify_status']
        if 'verify_type' in response:
            self.verify_type = response['verify_type']
