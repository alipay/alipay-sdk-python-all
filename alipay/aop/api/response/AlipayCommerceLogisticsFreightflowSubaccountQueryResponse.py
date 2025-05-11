#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLogisticsFreightflowSubaccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsFreightflowSubaccountQueryResponse, self).__init__()
        self._account_balance = None

    @property
    def account_balance(self):
        return self._account_balance

    @account_balance.setter
    def account_balance(self, value):
        self._account_balance = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsFreightflowSubaccountQueryResponse, self).parse_response_content(response_content)
        if 'account_balance' in response:
            self.account_balance = response['account_balance']
