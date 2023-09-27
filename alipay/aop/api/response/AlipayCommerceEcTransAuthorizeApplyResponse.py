#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcTransAuthorizeApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcTransAuthorizeApplyResponse, self).__init__()
        self._enterprise_id = None
        self._sign_url = None

    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def sign_url(self):
        return self._sign_url

    @sign_url.setter
    def sign_url(self, value):
        self._sign_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcTransAuthorizeApplyResponse, self).parse_response_content(response_content)
        if 'enterprise_id' in response:
            self.enterprise_id = response['enterprise_id']
        if 'sign_url' in response:
            self.sign_url = response['sign_url']
