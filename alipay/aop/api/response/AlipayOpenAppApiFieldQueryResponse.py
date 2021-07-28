#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AuthFieldResponse import AuthFieldResponse


class AlipayOpenAppApiFieldQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppApiFieldQueryResponse, self).__init__()
        self._auth_field_response = None

    @property
    def auth_field_response(self):
        return self._auth_field_response

    @auth_field_response.setter
    def auth_field_response(self, value):
        if isinstance(value, AuthFieldResponse):
            self._auth_field_response = value
        else:
            self._auth_field_response = AuthFieldResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppApiFieldQueryResponse, self).parse_response_content(response_content)
        if 'auth_field_response' in response:
            self.auth_field_response = response['auth_field_response']
