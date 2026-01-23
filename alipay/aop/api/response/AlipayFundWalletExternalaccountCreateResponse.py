#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundWalletExternalaccountCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundWalletExternalaccountCreateResponse, self).__init__()
        self._external_account_no = None
        self._user_wallet_id = None

    @property
    def external_account_no(self):
        return self._external_account_no

    @external_account_no.setter
    def external_account_no(self, value):
        self._external_account_no = value
    @property
    def user_wallet_id(self):
        return self._user_wallet_id

    @user_wallet_id.setter
    def user_wallet_id(self, value):
        self._user_wallet_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundWalletExternalaccountCreateResponse, self).parse_response_content(response_content)
        if 'external_account_no' in response:
            self.external_account_no = response['external_account_no']
        if 'user_wallet_id' in response:
            self.user_wallet_id = response['user_wallet_id']
