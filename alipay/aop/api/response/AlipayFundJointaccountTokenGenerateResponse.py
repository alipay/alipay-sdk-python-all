#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundJointaccountTokenGenerateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundJointaccountTokenGenerateResponse, self).__init__()
        self._token_key = None

    @property
    def token_key(self):
        return self._token_key

    @token_key.setter
    def token_key(self, value):
        self._token_key = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundJointaccountTokenGenerateResponse, self).parse_response_content(response_content)
        if 'token_key' in response:
            self.token_key = response['token_key']
