#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeOrderPayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeOrderPayResponse, self).__init__()
        self._async_payment_mode = None
        self._gmt_payment = None
        self._out_request_no = None
        self._out_trade_no = None
        self._total_amount = None
        self._trade_no = None

    @property
    def async_payment_mode(self):
        return self._async_payment_mode

    @async_payment_mode.setter
    def async_payment_mode(self, value):
        self._async_payment_mode = value
    @property
    def gmt_payment(self):
        return self._gmt_payment

    @gmt_payment.setter
    def gmt_payment(self, value):
        self._gmt_payment = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayTradeOrderPayResponse, self).parse_response_content(response_content)
        if 'async_payment_mode' in response:
            self.async_payment_mode = response['async_payment_mode']
        if 'gmt_payment' in response:
            self.gmt_payment = response['gmt_payment']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
