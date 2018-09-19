#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeOrderinfoSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeOrderinfoSyncResponse, self).__init__()
        self._buyer_user_id = None
        self._out_trade_no = None
        self._trade_no = None

    @property
    def buyer_user_id(self):
        return self._buyer_user_id

    @buyer_user_id.setter
    def buyer_user_id(self, value):
        self._buyer_user_id = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeOrderinfoSyncResponse, self).parse_response_content(response_content)
        if 'buyer_user_id' in response:
            self.buyer_user_id = response['buyer_user_id']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
