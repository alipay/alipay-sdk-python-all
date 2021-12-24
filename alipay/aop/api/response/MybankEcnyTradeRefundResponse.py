#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankEcnyTradeRefundResponse(AlipayResponse):

    def __init__(self):
        super(MybankEcnyTradeRefundResponse, self).__init__()
        self._fund_change = None
        self._out_trade_no = None
        self._refund_fee = None
        self._trade_no = None

    @property
    def fund_change(self):
        return self._fund_change

    @fund_change.setter
    def fund_change(self, value):
        self._fund_change = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def refund_fee(self):
        return self._refund_fee

    @refund_fee.setter
    def refund_fee(self, value):
        self._refund_fee = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(MybankEcnyTradeRefundResponse, self).parse_response_content(response_content)
        if 'fund_change' in response:
            self.fund_change = response['fund_change']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'refund_fee' in response:
            self.refund_fee = response['refund_fee']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
