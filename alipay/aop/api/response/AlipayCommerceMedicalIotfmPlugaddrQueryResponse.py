#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalIotfmPlugaddrQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalIotfmPlugaddrQueryResponse, self).__init__()
        self._access_token = None
        self._url = None

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalIotfmPlugaddrQueryResponse, self).parse_response_content(response_content)
        if 'access_token' in response:
            self.access_token = response['access_token']
        if 'url' in response:
            self.url = response['url']
