#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateSceneTokenCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateSceneTokenCreateResponse, self).__init__()
        self._token = None

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateSceneTokenCreateResponse, self).parse_response_content(response_content)
        if 'token' in response:
            self.token = response['token']
