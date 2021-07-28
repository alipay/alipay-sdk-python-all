#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeSettleConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSettleConfirmResponse, self).__init__()
        self._out_request_no = None
        self._settle_amount = None
        self._trade_no = None

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
        response = super(AlipayTradeSettleConfirmResponse, self).parse_response_content(response_content)
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'settle_amount' in response:
            self.settle_amount = response['settle_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
