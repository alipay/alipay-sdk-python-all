#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLogisticsFreightflowSubaccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsFreightflowSubaccountQueryResponse, self).__init__()
        self._account_balance = None
        self._actual_balance = None
        self._freeze_amt = None

    @property
    def account_balance(self):
        return self._account_balance

    @account_balance.setter
    def account_balance(self, value):
        self._account_balance = value
    @property
    def actual_balance(self):
        return self._actual_balance

    @actual_balance.setter
    def actual_balance(self, value):
        self._actual_balance = value
    @property
    def freeze_amt(self):
        return self._freeze_amt

    @freeze_amt.setter
    def freeze_amt(self, value):
        self._freeze_amt = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsFreightflowSubaccountQueryResponse, self).parse_response_content(response_content)
        if 'account_balance' in response:
            self.account_balance = response['account_balance']
        if 'actual_balance' in response:
            self.actual_balance = response['actual_balance']
        if 'freeze_amt' in response:
            self.freeze_amt = response['freeze_amt']
