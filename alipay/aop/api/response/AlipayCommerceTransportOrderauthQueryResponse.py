#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportOrderauthQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportOrderauthQueryResponse, self).__init__()
        self._auth_status = None

    @property
    def auth_status(self):
        return self._auth_status

    @auth_status.setter
    def auth_status(self, value):
        self._auth_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportOrderauthQueryResponse, self).parse_response_content(response_content)
        if 'auth_status' in response:
            self.auth_status = response['auth_status']
