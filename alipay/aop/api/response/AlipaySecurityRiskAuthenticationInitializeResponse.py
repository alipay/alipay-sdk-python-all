#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskAuthenticationInitializeResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskAuthenticationInitializeResponse, self).__init__()
        self._biz_result = None
        self._token_id = None

    @property
    def biz_result(self):
        return self._biz_result

    @biz_result.setter
    def biz_result(self, value):
        self._biz_result = value
    @property
    def token_id(self):
        return self._token_id

    @token_id.setter
    def token_id(self, value):
        self._token_id = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskAuthenticationInitializeResponse, self).parse_response_content(response_content)
        if 'biz_result' in response:
            self.biz_result = response['biz_result']
        if 'token_id' in response:
            self.token_id = response['token_id']
