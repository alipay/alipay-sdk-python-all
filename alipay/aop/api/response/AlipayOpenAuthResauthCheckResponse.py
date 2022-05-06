#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAuthResauthCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAuthResauthCheckResponse, self).__init__()
        self._auth_status = None

    @property
    def auth_status(self):
        return self._auth_status

    @auth_status.setter
    def auth_status(self, value):
        self._auth_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAuthResauthCheckResponse, self).parse_response_content(response_content)
        if 'auth_status' in response:
            self.auth_status = response['auth_status']
