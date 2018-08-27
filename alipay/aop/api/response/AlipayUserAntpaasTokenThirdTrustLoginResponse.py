#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAntpaasTokenThirdTrustLoginResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAntpaasTokenThirdTrustLoginResponse, self).__init__()
        self._third_trust_token = None

    @property
    def third_trust_token(self):
        return self._third_trust_token

    @third_trust_token.setter
    def third_trust_token(self, value):
        self._third_trust_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAntpaasTokenThirdTrustLoginResponse, self).parse_response_content(response_content)
        if 'third_trust_token' in response:
            self.third_trust_token = response['third_trust_token']
