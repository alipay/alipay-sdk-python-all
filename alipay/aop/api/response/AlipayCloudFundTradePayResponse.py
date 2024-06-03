#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudFundTradePayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudFundTradePayResponse, self).__init__()
        self._buyer_logon_id = None
        self._buyer_open_id = None
        self._buyer_user_id = None
        self._can_turn_to_app_pay = None
        self._out_trade_no = None
        self._total_amount = None
        self._trade_no = None

    @property
    def buyer_logon_id(self):
        return self._buyer_logon_id

    @buyer_logon_id.setter
    def buyer_logon_id(self, value):
        self._buyer_logon_id = value
    @property
    def buyer_open_id(self):
        return self._buyer_open_id

    @buyer_open_id.setter
    def buyer_open_id(self, value):
        self._buyer_open_id = value
    @property
    def buyer_user_id(self):
        return self._buyer_user_id

    @buyer_user_id.setter
    def buyer_user_id(self, value):
        self._buyer_user_id = value
    @property
    def can_turn_to_app_pay(self):
        return self._can_turn_to_app_pay

    @can_turn_to_app_pay.setter
    def can_turn_to_app_pay(self, value):
        self._can_turn_to_app_pay = value
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
        response = super(AlipayCloudFundTradePayResponse, self).parse_response_content(response_content)
        if 'buyer_logon_id' in response:
            self.buyer_logon_id = response['buyer_logon_id']
        if 'buyer_open_id' in response:
            self.buyer_open_id = response['buyer_open_id']
        if 'buyer_user_id' in response:
            self.buyer_user_id = response['buyer_user_id']
        if 'can_turn_to_app_pay' in response:
            self.can_turn_to_app_pay = response['can_turn_to_app_pay']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
