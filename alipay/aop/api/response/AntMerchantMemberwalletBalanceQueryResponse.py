#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantMemberwalletBalanceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantMemberwalletBalanceQueryResponse, self).__init__()
        self._balance = None
        self._benefit_balance = None
        self._principal_balance = None

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def benefit_balance(self):
        return self._benefit_balance

    @benefit_balance.setter
    def benefit_balance(self, value):
        self._benefit_balance = value
    @property
    def principal_balance(self):
        return self._principal_balance

    @principal_balance.setter
    def principal_balance(self, value):
        self._principal_balance = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantMemberwalletBalanceQueryResponse, self).parse_response_content(response_content)
        if 'balance' in response:
            self.balance = response['balance']
        if 'benefit_balance' in response:
            self.benefit_balance = response['benefit_balance']
        if 'principal_balance' in response:
            self.principal_balance = response['principal_balance']
