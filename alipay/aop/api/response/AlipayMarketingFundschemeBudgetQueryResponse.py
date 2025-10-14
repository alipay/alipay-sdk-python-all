#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingFundschemeBudgetQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingFundschemeBudgetQueryResponse, self).__init__()
        self._balance = None
        self._fund_scheme_id = None
        self._total_amount = None

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def fund_scheme_id(self):
        return self._fund_scheme_id

    @fund_scheme_id.setter
    def fund_scheme_id(self, value):
        self._fund_scheme_id = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingFundschemeBudgetQueryResponse, self).parse_response_content(response_content)
        if 'balance' in response:
            self.balance = response['balance']
        if 'fund_scheme_id' in response:
            self.fund_scheme_id = response['fund_scheme_id']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
