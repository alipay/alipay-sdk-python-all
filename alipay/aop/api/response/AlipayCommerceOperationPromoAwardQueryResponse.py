#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationPromoAwardQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationPromoAwardQueryResponse, self).__init__()
        self._award_amount = None
        self._sign_up_id = None
        self._trade_count = None

    @property
    def award_amount(self):
        return self._award_amount

    @award_amount.setter
    def award_amount(self, value):
        self._award_amount = value
    @property
    def sign_up_id(self):
        return self._sign_up_id

    @sign_up_id.setter
    def sign_up_id(self, value):
        self._sign_up_id = value
    @property
    def trade_count(self):
        return self._trade_count

    @trade_count.setter
    def trade_count(self, value):
        self._trade_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationPromoAwardQueryResponse, self).parse_response_content(response_content)
        if 'award_amount' in response:
            self.award_amount = response['award_amount']
        if 'sign_up_id' in response:
            self.sign_up_id = response['sign_up_id']
        if 'trade_count' in response:
            self.trade_count = response['trade_count']
