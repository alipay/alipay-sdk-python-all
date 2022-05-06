#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommercePayforprivilegeWithdrawamountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommercePayforprivilegeWithdrawamountQueryResponse, self).__init__()
        self._balance = None
        self._withdraw_balance = None

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def withdraw_balance(self):
        return self._withdraw_balance

    @withdraw_balance.setter
    def withdraw_balance(self, value):
        self._withdraw_balance = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommercePayforprivilegeWithdrawamountQueryResponse, self).parse_response_content(response_content)
        if 'balance' in response:
            self.balance = response['balance']
        if 'withdraw_balance' in response:
            self.withdraw_balance = response['withdraw_balance']
