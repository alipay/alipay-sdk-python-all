#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportPromoTasklistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportPromoTasklistQueryResponse, self).__init__()
        self._prize = None
        self._prize_price = None

    @property
    def prize(self):
        return self._prize

    @prize.setter
    def prize(self, value):
        self._prize = value
    @property
    def prize_price(self):
        return self._prize_price

    @prize_price.setter
    def prize_price(self, value):
        self._prize_price = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportPromoTasklistQueryResponse, self).parse_response_content(response_content)
        if 'prize' in response:
            self.prize = response['prize']
        if 'prize_price' in response:
            self.prize_price = response['prize_price']
