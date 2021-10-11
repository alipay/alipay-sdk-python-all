#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankPaymentTradeSubaccountBalanceQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankPaymentTradeSubaccountBalanceQueryResponse, self).__init__()
        self._available_balance = None
        self._currency_value = None
        self._sub_card_no = None

    @property
    def available_balance(self):
        return self._available_balance

    @available_balance.setter
    def available_balance(self, value):
        self._available_balance = value
    @property
    def currency_value(self):
        return self._currency_value

    @currency_value.setter
    def currency_value(self, value):
        self._currency_value = value
    @property
    def sub_card_no(self):
        return self._sub_card_no

    @sub_card_no.setter
    def sub_card_no(self, value):
        self._sub_card_no = value

    def parse_response_content(self, response_content):
        response = super(MybankPaymentTradeSubaccountBalanceQueryResponse, self).parse_response_content(response_content)
        if 'available_balance' in response:
            self.available_balance = response['available_balance']
        if 'currency_value' in response:
            self.currency_value = response['currency_value']
        if 'sub_card_no' in response:
            self.sub_card_no = response['sub_card_no']
