#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFinancialnetAuthBalanceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinancialnetAuthBalanceQueryResponse, self).__init__()
        self._account_balance = None
        self._currency = None
        self._result_code = None
        self._result_desc = None
        self._success = None

    @property
    def account_balance(self):
        return self._account_balance

    @account_balance.setter
    def account_balance(self, value):
        self._account_balance = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_desc(self):
        return self._result_desc

    @result_desc.setter
    def result_desc(self, value):
        self._result_desc = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayFinancialnetAuthBalanceQueryResponse, self).parse_response_content(response_content)
        if 'account_balance' in response:
            self.account_balance = response['account_balance']
        if 'currency' in response:
            self.currency = response['currency']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_desc' in response:
            self.result_desc = response['result_desc']
        if 'success' in response:
            self.success = response['success']
