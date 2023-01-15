#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceYuntaskAccountbookWithdrawResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceYuntaskAccountbookWithdrawResponse, self).__init__()
        self._amount = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceYuntaskAccountbookWithdrawResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
