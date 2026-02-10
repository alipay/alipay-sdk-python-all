#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportTrafficshareTradeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportTrafficshareTradeQueryResponse, self).__init__()
        self._amount_unit = None
        self._discount_amount = None
        self._order_no = None
        self._pay_amount = None
        self._pay_time = None
        self._receipt_amount = None
        self._total_amount = None
        self._trade_no = None
        self._trade_status = None

    @property
    def amount_unit(self):
        return self._amount_unit

    @amount_unit.setter
    def amount_unit(self, value):
        self._amount_unit = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def receipt_amount(self):
        return self._receipt_amount

    @receipt_amount.setter
    def receipt_amount(self, value):
        self._receipt_amount = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_status(self):
        return self._trade_status

    @trade_status.setter
    def trade_status(self, value):
        self._trade_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportTrafficshareTradeQueryResponse, self).parse_response_content(response_content)
        if 'amount_unit' in response:
            self.amount_unit = response['amount_unit']
        if 'discount_amount' in response:
            self.discount_amount = response['discount_amount']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'pay_amount' in response:
            self.pay_amount = response['pay_amount']
        if 'pay_time' in response:
            self.pay_time = response['pay_time']
        if 'receipt_amount' in response:
            self.receipt_amount = response['receipt_amount']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
        if 'trade_status' in response:
            self.trade_status = response['trade_status']
