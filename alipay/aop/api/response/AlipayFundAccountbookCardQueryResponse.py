#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundAccountbookCardQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundAccountbookCardQueryResponse, self).__init__()
        self._account_book_card_no = None
        self._available_amount = None
        self._bank_acc_name = None
        self._card_bank = None
        self._card_branch = None
        self._card_deposit = None
        self._card_location = None
        self._status = None

    @property
    def account_book_card_no(self):
        return self._account_book_card_no

    @account_book_card_no.setter
    def account_book_card_no(self, value):
        self._account_book_card_no = value
    @property
    def available_amount(self):
        return self._available_amount

    @available_amount.setter
    def available_amount(self, value):
        self._available_amount = value
    @property
    def bank_acc_name(self):
        return self._bank_acc_name

    @bank_acc_name.setter
    def bank_acc_name(self, value):
        self._bank_acc_name = value
    @property
    def card_bank(self):
        return self._card_bank

    @card_bank.setter
    def card_bank(self, value):
        self._card_bank = value
    @property
    def card_branch(self):
        return self._card_branch

    @card_branch.setter
    def card_branch(self, value):
        self._card_branch = value
    @property
    def card_deposit(self):
        return self._card_deposit

    @card_deposit.setter
    def card_deposit(self, value):
        self._card_deposit = value
    @property
    def card_location(self):
        return self._card_location

    @card_location.setter
    def card_location(self, value):
        self._card_location = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundAccountbookCardQueryResponse, self).parse_response_content(response_content)
        if 'account_book_card_no' in response:
            self.account_book_card_no = response['account_book_card_no']
        if 'available_amount' in response:
            self.available_amount = response['available_amount']
        if 'bank_acc_name' in response:
            self.bank_acc_name = response['bank_acc_name']
        if 'card_bank' in response:
            self.card_bank = response['card_bank']
        if 'card_branch' in response:
            self.card_branch = response['card_branch']
        if 'card_deposit' in response:
            self.card_deposit = response['card_deposit']
        if 'card_location' in response:
            self.card_location = response['card_location']
        if 'status' in response:
            self.status = response['status']
