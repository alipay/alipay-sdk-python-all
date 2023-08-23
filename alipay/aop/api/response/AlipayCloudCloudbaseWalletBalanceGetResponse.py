#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseWalletBalanceGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseWalletBalanceGetResponse, self).__init__()
        self._available_amount = None
        self._unpaid_amount = None
        self._wallet_amount = None

    @property
    def available_amount(self):
        return self._available_amount

    @available_amount.setter
    def available_amount(self, value):
        self._available_amount = value
    @property
    def unpaid_amount(self):
        return self._unpaid_amount

    @unpaid_amount.setter
    def unpaid_amount(self, value):
        self._unpaid_amount = value
    @property
    def wallet_amount(self):
        return self._wallet_amount

    @wallet_amount.setter
    def wallet_amount(self, value):
        self._wallet_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseWalletBalanceGetResponse, self).parse_response_content(response_content)
        if 'available_amount' in response:
            self.available_amount = response['available_amount']
        if 'unpaid_amount' in response:
            self.unpaid_amount = response['unpaid_amount']
        if 'wallet_amount' in response:
            self.wallet_amount = response['wallet_amount']
