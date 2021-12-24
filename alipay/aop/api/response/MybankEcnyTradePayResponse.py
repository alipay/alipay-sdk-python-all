#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankEcnyTradePayResponse(AlipayResponse):

    def __init__(self):
        super(MybankEcnyTradePayResponse, self).__init__()
        self._buyer_wallet_id = None
        self._buyer_wallet_name = None
        self._gmt_payment = None
        self._out_trade_no = None
        self._total_amount = None
        self._trade_no = None

    @property
    def buyer_wallet_id(self):
        return self._buyer_wallet_id

    @buyer_wallet_id.setter
    def buyer_wallet_id(self, value):
        self._buyer_wallet_id = value
    @property
    def buyer_wallet_name(self):
        return self._buyer_wallet_name

    @buyer_wallet_name.setter
    def buyer_wallet_name(self, value):
        self._buyer_wallet_name = value
    @property
    def gmt_payment(self):
        return self._gmt_payment

    @gmt_payment.setter
    def gmt_payment(self, value):
        self._gmt_payment = value
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
        response = super(MybankEcnyTradePayResponse, self).parse_response_content(response_content)
        if 'buyer_wallet_id' in response:
            self.buyer_wallet_id = response['buyer_wallet_id']
        if 'buyer_wallet_name' in response:
            self.buyer_wallet_name = response['buyer_wallet_name']
        if 'gmt_payment' in response:
            self.gmt_payment = response['gmt_payment']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
