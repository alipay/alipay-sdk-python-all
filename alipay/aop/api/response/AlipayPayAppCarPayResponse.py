#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPayAppCarPayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayAppCarPayResponse, self).__init__()
        self._context_token = None

    @property
    def context_token(self):
        return self._context_token

    @context_token.setter
    def context_token(self, value):
        self._context_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayPayAppCarPayResponse, self).parse_response_content(response_content)
        if 'context_token' in response:
            self.context_token = response['context_token']
