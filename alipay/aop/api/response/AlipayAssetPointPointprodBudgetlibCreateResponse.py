#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAssetPointPointprodBudgetlibCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAssetPointPointprodBudgetlibCreateResponse, self).__init__()
        self._balance = None
        self._budget_code = None
        self._message = None

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def budget_code(self):
        return self._budget_code

    @budget_code.setter
    def budget_code(self, value):
        self._budget_code = value
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    def parse_response_content(self, response_content):
        response = super(AlipayAssetPointPointprodBudgetlibCreateResponse, self).parse_response_content(response_content)
        if 'balance' in response:
            self.balance = response['balance']
        if 'budget_code' in response:
            self.budget_code = response['budget_code']
        if 'message' in response:
            self.message = response['message']
