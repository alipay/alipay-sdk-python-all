#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundZcardprodUserBindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundZcardprodUserBindResponse, self).__init__()
        self._bind_token = None

    @property
    def bind_token(self):
        return self._bind_token

    @bind_token.setter
    def bind_token(self, value):
        self._bind_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundZcardprodUserBindResponse, self).parse_response_content(response_content)
        if 'bind_token' in response:
            self.bind_token = response['bind_token']
