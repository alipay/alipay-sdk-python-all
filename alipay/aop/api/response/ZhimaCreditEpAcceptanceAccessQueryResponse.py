#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpAcceptanceAccessQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpAcceptanceAccessQueryResponse, self).__init__()
        self._access_token = None
        self._access_url = None

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value
    @property
    def access_url(self):
        return self._access_url

    @access_url.setter
    def access_url(self, value):
        self._access_url = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpAcceptanceAccessQueryResponse, self).parse_response_content(response_content)
        if 'access_token' in response:
            self.access_token = response['access_token']
        if 'access_url' in response:
            self.access_url = response['access_url']
