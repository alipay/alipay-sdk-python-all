#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingToolSignupQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingToolSignupQueryResponse, self).__init__()
        self._play_id = None
        self._sign_up = None

    @property
    def play_id(self):
        return self._play_id

    @play_id.setter
    def play_id(self, value):
        self._play_id = value
    @property
    def sign_up(self):
        return self._sign_up

    @sign_up.setter
    def sign_up(self, value):
        self._sign_up = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingToolSignupQueryResponse, self).parse_response_content(response_content)
        if 'play_id' in response:
            self.play_id = response['play_id']
        if 'sign_up' in response:
            self.sign_up = response['sign_up']
