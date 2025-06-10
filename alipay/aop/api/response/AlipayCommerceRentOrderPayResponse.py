#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRentOrderPayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentOrderPayResponse, self).__init__()
        self._order_id = None
        self._out_trade_no = None
        self._pay_amount = None
        self._trade_no = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentOrderPayResponse, self).parse_response_content(response_content)
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'pay_amount' in response:
            self.pay_amount = response['pay_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
