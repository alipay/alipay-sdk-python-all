#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundTransAuctionBalanceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTransAuctionBalanceQueryResponse, self).__init__()
        self._balance_available = None
        self._balance_freezed = None

    @property
    def balance_available(self):
        return self._balance_available

    @balance_available.setter
    def balance_available(self, value):
        self._balance_available = value
    @property
    def balance_freezed(self):
        return self._balance_freezed

    @balance_freezed.setter
    def balance_freezed(self, value):
        self._balance_freezed = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundTransAuctionBalanceQueryResponse, self).parse_response_content(response_content)
        if 'balance_available' in response:
            self.balance_available = response['balance_available']
        if 'balance_freezed' in response:
            self.balance_freezed = response['balance_freezed']
