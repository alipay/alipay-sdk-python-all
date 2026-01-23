#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationCarservicesaastldcAuthenticationQuerystatusResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationCarservicesaastldcAuthenticationQuerystatusResponse, self).__init__()
        self._auth_no = None
        self._auth_result = None
        self._auth_type = None

    @property
    def auth_no(self):
        return self._auth_no

    @auth_no.setter
    def auth_no(self, value):
        self._auth_no = value
    @property
    def auth_result(self):
        return self._auth_result

    @auth_result.setter
    def auth_result(self, value):
        self._auth_result = value
    @property
    def auth_type(self):
        return self._auth_type

    @auth_type.setter
    def auth_type(self, value):
        self._auth_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationCarservicesaastldcAuthenticationQuerystatusResponse, self).parse_response_content(response_content)
        if 'auth_no' in response:
            self.auth_no = response['auth_no']
        if 'auth_result' in response:
            self.auth_result = response['auth_result']
        if 'auth_type' in response:
            self.auth_type = response['auth_type']
