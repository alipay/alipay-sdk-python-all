#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsInsmopRetainQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsInsmopRetainQueryResponse, self).__init__()
        self._pass_token = None

    @property
    def pass_token(self):
        return self._pass_token

    @pass_token.setter
    def pass_token(self, value):
        self._pass_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsInsmopRetainQueryResponse, self).parse_response_content(response_content)
        if 'pass_token' in response:
            self.pass_token = response['pass_token']
