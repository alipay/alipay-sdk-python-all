#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeOverseasSettleResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeOverseasSettleResponse, self).__init__()
        self._exchange_rate = None
        self._foreign_settle_amount = None
        self._foreign_settle_currency = None
        self._out_request_no = None
        self._settle_amount = None
        self._trade_no = None

    @property
    def exchange_rate(self):
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, value):
        self._exchange_rate = value
    @property
    def foreign_settle_amount(self):
        return self._foreign_settle_amount

    @foreign_settle_amount.setter
    def foreign_settle_amount(self, value):
        self._foreign_settle_amount = value
    @property
    def foreign_settle_currency(self):
        return self._foreign_settle_currency

    @foreign_settle_currency.setter
    def foreign_settle_currency(self, value):
        self._foreign_settle_currency = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def settle_amount(self):
        return self._settle_amount

    @settle_amount.setter
    def settle_amount(self, value):
        self._settle_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeOverseasSettleResponse, self).parse_response_content(response_content)
        if 'exchange_rate' in response:
            self.exchange_rate = response['exchange_rate']
        if 'foreign_settle_amount' in response:
            self.foreign_settle_amount = response['foreign_settle_amount']
        if 'foreign_settle_currency' in response:
            self.foreign_settle_currency = response['foreign_settle_currency']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'settle_amount' in response:
            self.settle_amount = response['settle_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
