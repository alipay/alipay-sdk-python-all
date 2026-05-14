#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryEducertifyTokenCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryEducertifyTokenCreateResponse, self).__init__()
        self._certify_token = None

    @property
    def certify_token(self):
        return self._certify_token

    @certify_token.setter
    def certify_token(self, value):
        self._certify_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryEducertifyTokenCreateResponse, self).parse_response_content(response_content)
        if 'certify_token' in response:
            self.certify_token = response['certify_token']
