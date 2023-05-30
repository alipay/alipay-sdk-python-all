#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFinancialnetAuthEcsignSealAuthResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinancialnetAuthEcsignSealAuthResponse, self).__init__()
        self._auth_jump_url = None

    @property
    def auth_jump_url(self):
        return self._auth_jump_url

    @auth_jump_url.setter
    def auth_jump_url(self, value):
        self._auth_jump_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayFinancialnetAuthEcsignSealAuthResponse, self).parse_response_content(response_content)
        if 'auth_jump_url' in response:
            self.auth_jump_url = response['auth_jump_url']
