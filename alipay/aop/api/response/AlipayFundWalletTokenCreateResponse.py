#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundWalletTokenCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundWalletTokenCreateResponse, self).__init__()
        self._bind_token = None
        self._bind_url = None
        self._user_wallet_id = None

    @property
    def bind_token(self):
        return self._bind_token

    @bind_token.setter
    def bind_token(self, value):
        self._bind_token = value
    @property
    def bind_url(self):
        return self._bind_url

    @bind_url.setter
    def bind_url(self, value):
        self._bind_url = value
    @property
    def user_wallet_id(self):
        return self._user_wallet_id

    @user_wallet_id.setter
    def user_wallet_id(self, value):
        self._user_wallet_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundWalletTokenCreateResponse, self).parse_response_content(response_content)
        if 'bind_token' in response:
            self.bind_token = response['bind_token']
        if 'bind_url' in response:
            self.bind_url = response['bind_url']
        if 'user_wallet_id' in response:
            self.user_wallet_id = response['user_wallet_id']
