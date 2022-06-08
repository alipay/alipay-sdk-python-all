#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundEnterprisepayUnsignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundEnterprisepayUnsignResponse, self).__init__()
        self._unsign_token = None
        self._unsign_url = None

    @property
    def unsign_token(self):
        return self._unsign_token

    @unsign_token.setter
    def unsign_token(self, value):
        self._unsign_token = value
    @property
    def unsign_url(self):
        return self._unsign_url

    @unsign_url.setter
    def unsign_url(self, value):
        self._unsign_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundEnterprisepayUnsignResponse, self).parse_response_content(response_content)
        if 'unsign_token' in response:
            self.unsign_token = response['unsign_token']
        if 'unsign_url' in response:
            self.unsign_url = response['unsign_url']
