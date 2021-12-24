#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppAccountBalanceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppAccountBalanceQueryResponse, self).__init__()
        self._account = None
        self._available_money = None
        self._balance = None
        self._date = None
        self._freeze_money = None
        self._request_time = None

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value
    @property
    def available_money(self):
        return self._available_money

    @available_money.setter
    def available_money(self, value):
        self._available_money = value
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def freeze_money(self):
        return self._freeze_money

    @freeze_money.setter
    def freeze_money(self, value):
        self._freeze_money = value
    @property
    def request_time(self):
        return self._request_time

    @request_time.setter
    def request_time(self, value):
        self._request_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppAccountBalanceQueryResponse, self).parse_response_content(response_content)
        if 'account' in response:
            self.account = response['account']
        if 'available_money' in response:
            self.available_money = response['available_money']
        if 'balance' in response:
            self.balance = response['balance']
        if 'date' in response:
            self.date = response['date']
        if 'freeze_money' in response:
            self.freeze_money = response['freeze_money']
        if 'request_time' in response:
            self.request_time = response['request_time']
