#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcEmployeeInviteQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcEmployeeInviteQueryResponse, self).__init__()
        self._enterprise_id = None
        self._mini_app_sign_url = None
        self._share_code = None
        self._sign_url = None

    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def mini_app_sign_url(self):
        return self._mini_app_sign_url

    @mini_app_sign_url.setter
    def mini_app_sign_url(self, value):
        self._mini_app_sign_url = value
    @property
    def share_code(self):
        return self._share_code

    @share_code.setter
    def share_code(self, value):
        self._share_code = value
    @property
    def sign_url(self):
        return self._sign_url

    @sign_url.setter
    def sign_url(self, value):
        self._sign_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcEmployeeInviteQueryResponse, self).parse_response_content(response_content)
        if 'enterprise_id' in response:
            self.enterprise_id = response['enterprise_id']
        if 'mini_app_sign_url' in response:
            self.mini_app_sign_url = response['mini_app_sign_url']
        if 'share_code' in response:
            self.share_code = response['share_code']
        if 'sign_url' in response:
            self.sign_url = response['sign_url']
