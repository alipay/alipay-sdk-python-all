#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeFastpayEteDidiPayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeFastpayEteDidiPayResponse, self).__init__()
        self._out_trade_no = None
        self._seller_id = None
        self._total_fee = None
        self._trade_no = None

    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def total_fee(self):
        return self._total_fee

    @total_fee.setter
    def total_fee(self, value):
        self._total_fee = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeFastpayEteDidiPayResponse, self).parse_response_content(response_content)
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'seller_id' in response:
            self.seller_id = response['seller_id']
        if 'total_fee' in response:
            self.total_fee = response['total_fee']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
