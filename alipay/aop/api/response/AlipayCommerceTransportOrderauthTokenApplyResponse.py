#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportOrderauthTokenApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportOrderauthTokenApplyResponse, self).__init__()
        self._industry_auth_token = None

    @property
    def industry_auth_token(self):
        return self._industry_auth_token

    @industry_auth_token.setter
    def industry_auth_token(self, value):
        self._industry_auth_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportOrderauthTokenApplyResponse, self).parse_response_content(response_content)
        if 'industry_auth_token' in response:
            self.industry_auth_token = response['industry_auth_token']
