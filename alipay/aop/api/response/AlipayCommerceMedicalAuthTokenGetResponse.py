#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AuthResult import AuthResult


class AlipayCommerceMedicalAuthTokenGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalAuthTokenGetResponse, self).__init__()
        self._auth_result = None

    @property
    def auth_result(self):
        return self._auth_result

    @auth_result.setter
    def auth_result(self, value):
        if isinstance(value, AuthResult):
            self._auth_result = value
        else:
            self._auth_result = AuthResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalAuthTokenGetResponse, self).parse_response_content(response_content)
        if 'auth_result' in response:
            self.auth_result = response['auth_result']
