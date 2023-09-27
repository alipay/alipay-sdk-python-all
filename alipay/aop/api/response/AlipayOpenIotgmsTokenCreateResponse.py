#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenIotgmsTokenCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenIotgmsTokenCreateResponse, self).__init__()
        self._query_token = None

    @property
    def query_token(self):
        return self._query_token

    @query_token.setter
    def query_token(self, value):
        self._query_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenIotgmsTokenCreateResponse, self).parse_response_content(response_content)
        if 'query_token' in response:
            self.query_token = response['query_token']
