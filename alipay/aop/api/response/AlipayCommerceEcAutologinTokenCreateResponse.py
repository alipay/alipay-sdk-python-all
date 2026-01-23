#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcAutologinTokenCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcAutologinTokenCreateResponse, self).__init__()
        self._auto_login_token = None

    @property
    def auto_login_token(self):
        return self._auto_login_token

    @auto_login_token.setter
    def auto_login_token(self, value):
        self._auto_login_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcAutologinTokenCreateResponse, self).parse_response_content(response_content)
        if 'auto_login_token' in response:
            self.auto_login_token = response['auto_login_token']
