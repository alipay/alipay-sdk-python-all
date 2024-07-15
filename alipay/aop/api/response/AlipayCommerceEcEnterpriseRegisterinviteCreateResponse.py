#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcEnterpriseRegisterinviteCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcEnterpriseRegisterinviteCreateResponse, self).__init__()
        self._expire_time = None
        self._pc_invite_url = None

    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def pc_invite_url(self):
        return self._pc_invite_url

    @pc_invite_url.setter
    def pc_invite_url(self, value):
        self._pc_invite_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcEnterpriseRegisterinviteCreateResponse, self).parse_response_content(response_content)
        if 'expire_time' in response:
            self.expire_time = response['expire_time']
        if 'pc_invite_url' in response:
            self.pc_invite_url = response['pc_invite_url']
