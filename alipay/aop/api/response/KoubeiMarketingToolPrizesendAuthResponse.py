#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMarketingToolPrizesendAuthResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingToolPrizesendAuthResponse, self).__init__()
        self._token = None

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingToolPrizesendAuthResponse, self).parse_response_content(response_content)
        if 'token' in response:
            self.token = response['token']
