#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcRecyclinginvoiceBiztransferauthApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcRecyclinginvoiceBiztransferauthApplyResponse, self).__init__()
        self._auth_id = None
        self._auth_status = None
        self._auth_url = None

    @property
    def auth_id(self):
        return self._auth_id

    @auth_id.setter
    def auth_id(self, value):
        self._auth_id = value
    @property
    def auth_status(self):
        return self._auth_status

    @auth_status.setter
    def auth_status(self, value):
        self._auth_status = value
    @property
    def auth_url(self):
        return self._auth_url

    @auth_url.setter
    def auth_url(self, value):
        self._auth_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcRecyclinginvoiceBiztransferauthApplyResponse, self).parse_response_content(response_content)
        if 'auth_id' in response:
            self.auth_id = response['auth_id']
        if 'auth_status' in response:
            self.auth_status = response['auth_status']
        if 'auth_url' in response:
            self.auth_url = response['auth_url']
