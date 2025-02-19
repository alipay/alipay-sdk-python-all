#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderCollaborateAuthCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderCollaborateAuthCreateResponse, self).__init__()
        self._apply_auth_url = None
        self._auth_order_id = None

    @property
    def apply_auth_url(self):
        return self._apply_auth_url

    @apply_auth_url.setter
    def apply_auth_url(self, value):
        self._apply_auth_url = value
    @property
    def auth_order_id(self):
        return self._auth_order_id

    @auth_order_id.setter
    def auth_order_id(self, value):
        self._auth_order_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderCollaborateAuthCreateResponse, self).parse_response_content(response_content)
        if 'apply_auth_url' in response:
            self.apply_auth_url = response['apply_auth_url']
        if 'auth_order_id' in response:
            self.auth_order_id = response['auth_order_id']
