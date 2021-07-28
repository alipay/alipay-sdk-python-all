#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingToolSignupSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingToolSignupSubmitResponse, self).__init__()
        self._play_id = None

    @property
    def play_id(self):
        return self._play_id

    @play_id.setter
    def play_id(self, value):
        self._play_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingToolSignupSubmitResponse, self).parse_response_content(response_content)
        if 'play_id' in response:
            self.play_id = response['play_id']
