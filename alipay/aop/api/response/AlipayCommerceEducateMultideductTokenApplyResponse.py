#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateMultideductTokenApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateMultideductTokenApplyResponse, self).__init__()
        self._token_id = None

    @property
    def token_id(self):
        return self._token_id

    @token_id.setter
    def token_id(self, value):
        self._token_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateMultideductTokenApplyResponse, self).parse_response_content(response_content)
        if 'token_id' in response:
            self.token_id = response['token_id']
