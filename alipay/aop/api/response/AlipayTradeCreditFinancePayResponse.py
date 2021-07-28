#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeCreditFinancePayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeCreditFinancePayResponse, self).__init__()
        self._amount = None
        self._currency = None
        self._gmt_payment = None
        self._out_request_no = None
        self._status = None
        self._trade_buyer_id = None
        self._trade_no = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
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
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trade_buyer_id(self):
        return self._trade_buyer_id

    @trade_buyer_id.setter
    def trade_buyer_id(self, value):
        self._trade_buyer_id = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeCreditFinancePayResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'currency' in response:
            self.currency = response['currency']
        if 'gmt_payment' in response:
            self.gmt_payment = response['gmt_payment']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'status' in response:
            self.status = response['status']
        if 'trade_buyer_id' in response:
            self.trade_buyer_id = response['trade_buyer_id']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
