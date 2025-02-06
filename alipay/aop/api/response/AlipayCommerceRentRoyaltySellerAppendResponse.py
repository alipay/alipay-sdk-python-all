#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRentRoyaltySellerAppendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentRoyaltySellerAppendResponse, self).__init__()
        self._execute_amount = None
        self._installment_id = None
        self._trade_no = None

    @property
    def execute_amount(self):
        return self._execute_amount

    @execute_amount.setter
    def execute_amount(self, value):
        self._execute_amount = value
    @property
    def installment_id(self):
        return self._installment_id

    @installment_id.setter
    def installment_id(self, value):
        self._installment_id = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentRoyaltySellerAppendResponse, self).parse_response_content(response_content)
        if 'execute_amount' in response:
            self.execute_amount = response['execute_amount']
        if 'installment_id' in response:
            self.installment_id = response['installment_id']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
