#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceYuntaskAccountbookQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceYuntaskAccountbookQueryResponse, self).__init__()
        self._account_book_id = None
        self._available_amount = None
        self._card_no = None

    @property
    def account_book_id(self):
        return self._account_book_id

    @account_book_id.setter
    def account_book_id(self, value):
        self._account_book_id = value
    @property
    def available_amount(self):
        return self._available_amount

    @available_amount.setter
    def available_amount(self, value):
        self._available_amount = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceYuntaskAccountbookQueryResponse, self).parse_response_content(response_content)
        if 'account_book_id' in response:
            self.account_book_id = response['account_book_id']
        if 'available_amount' in response:
            self.available_amount = response['available_amount']
        if 'card_no' in response:
            self.card_no = response['card_no']
