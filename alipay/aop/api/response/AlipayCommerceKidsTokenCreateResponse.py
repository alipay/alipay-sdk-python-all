#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceKidsTokenCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceKidsTokenCreateResponse, self).__init__()
        self._expire_time = None
        self._kids_token = None

    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def kids_token(self):
        return self._kids_token

    @kids_token.setter
    def kids_token(self, value):
        self._kids_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceKidsTokenCreateResponse, self).parse_response_content(response_content)
        if 'expire_time' in response:
            self.expire_time = response['expire_time']
        if 'kids_token' in response:
            self.kids_token = response['kids_token']
