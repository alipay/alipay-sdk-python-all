#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateRosterIdentityBindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateRosterIdentityBindResponse, self).__init__()
        self._bind_alipay_account = None

    @property
    def bind_alipay_account(self):
        return self._bind_alipay_account

    @bind_alipay_account.setter
    def bind_alipay_account(self, value):
        self._bind_alipay_account = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateRosterIdentityBindResponse, self).parse_response_content(response_content)
        if 'bind_alipay_account' in response:
            self.bind_alipay_account = response['bind_alipay_account']
