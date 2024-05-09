#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudFundWalletWithdrawResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudFundWalletWithdrawResponse, self).__init__()
        self._bill_no = None
        self._user_wallet_id = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def user_wallet_id(self):
        return self._user_wallet_id

    @user_wallet_id.setter
    def user_wallet_id(self, value):
        self._user_wallet_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudFundWalletWithdrawResponse, self).parse_response_content(response_content)
        if 'bill_no' in response:
            self.bill_no = response['bill_no']
        if 'user_wallet_id' in response:
            self.user_wallet_id = response['user_wallet_id']
