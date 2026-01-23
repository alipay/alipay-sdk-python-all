#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundWalletModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundWalletModifyResponse, self).__init__()
        self._user_wallet_id = None
        self._wallet_name = None

    @property
    def user_wallet_id(self):
        return self._user_wallet_id

    @user_wallet_id.setter
    def user_wallet_id(self, value):
        self._user_wallet_id = value
    @property
    def wallet_name(self):
        return self._wallet_name

    @wallet_name.setter
    def wallet_name(self, value):
        self._wallet_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundWalletModifyResponse, self).parse_response_content(response_content)
        if 'user_wallet_id' in response:
            self.user_wallet_id = response['user_wallet_id']
        if 'wallet_name' in response:
            self.wallet_name = response['wallet_name']
