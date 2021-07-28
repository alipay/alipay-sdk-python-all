#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInstserviceTokenCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInstserviceTokenCreateResponse, self).__init__()
        self._sign_token = None

    @property
    def sign_token(self):
        return self._sign_token

    @sign_token.setter
    def sign_token(self, value):
        self._sign_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInstserviceTokenCreateResponse, self).parse_response_content(response_content)
        if 'sign_token' in response:
            self.sign_token = response['sign_token']
