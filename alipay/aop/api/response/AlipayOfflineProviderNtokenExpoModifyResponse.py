#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderNtokenExpoModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderNtokenExpoModifyResponse, self).__init__()
        self._ntoken = None

    @property
    def ntoken(self):
        return self._ntoken

    @ntoken.setter
    def ntoken(self, value):
        self._ntoken = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderNtokenExpoModifyResponse, self).parse_response_content(response_content)
        if 'ntoken' in response:
            self.ntoken = response['ntoken']
