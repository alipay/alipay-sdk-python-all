#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiDiscountBillQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiDiscountBillQueryResponse, self).__init__()
        self._charge_no = None
        self._discount_amount = None
        self._pay_trade_no = None
        self._trade_amount = None
        self._trade_time = None

    @property
    def charge_no(self):
        return self._charge_no

    @charge_no.setter
    def charge_no(self, value):
        self._charge_no = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def pay_trade_no(self):
        return self._pay_trade_no

    @pay_trade_no.setter
    def pay_trade_no(self, value):
        self._pay_trade_no = value
    @property
    def trade_amount(self):
        return self._trade_amount

    @trade_amount.setter
    def trade_amount(self, value):
        self._trade_amount = value
    @property
    def trade_time(self):
        return self._trade_time

    @trade_time.setter
    def trade_time(self, value):
        self._trade_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiDiscountBillQueryResponse, self).parse_response_content(response_content)
        if 'charge_no' in response:
            self.charge_no = response['charge_no']
        if 'discount_amount' in response:
            self.discount_amount = response['discount_amount']
        if 'pay_trade_no' in response:
            self.pay_trade_no = response['pay_trade_no']
        if 'trade_amount' in response:
            self.trade_amount = response['trade_amount']
        if 'trade_time' in response:
            self.trade_time = response['trade_time']
