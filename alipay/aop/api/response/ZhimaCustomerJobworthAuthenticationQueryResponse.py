#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCustomerJobworthAuthenticationQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerJobworthAuthenticationQueryResponse, self).__init__()
        self._identity_result = None
        self._identity_result_skip_url = None
        self._open_id = None
        self._token_status = None
        self._user_id = None

    @property
    def identity_result(self):
        return self._identity_result

    @identity_result.setter
    def identity_result(self, value):
        self._identity_result = value
    @property
    def identity_result_skip_url(self):
        return self._identity_result_skip_url

    @identity_result_skip_url.setter
    def identity_result_skip_url(self, value):
        self._identity_result_skip_url = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def token_status(self):
        return self._token_status

    @token_status.setter
    def token_status(self, value):
        self._token_status = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCustomerJobworthAuthenticationQueryResponse, self).parse_response_content(response_content)
        if 'identity_result' in response:
            self.identity_result = response['identity_result']
        if 'identity_result_skip_url' in response:
            self.identity_result_skip_url = response['identity_result_skip_url']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'token_status' in response:
            self.token_status = response['token_status']
        if 'user_id' in response:
            self.user_id = response['user_id']
