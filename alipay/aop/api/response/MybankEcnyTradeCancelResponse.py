#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankEcnyTradeCancelResponse(AlipayResponse):

    def __init__(self):
        super(MybankEcnyTradeCancelResponse, self).__init__()
        self._action = None
        self._out_trade_no = None
        self._retry_flag = None
        self._trade_no = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def retry_flag(self):
        return self._retry_flag

    @retry_flag.setter
    def retry_flag(self, value):
        self._retry_flag = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(MybankEcnyTradeCancelResponse, self).parse_response_content(response_content)
        if 'action' in response:
            self.action = response['action']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'retry_flag' in response:
            self.retry_flag = response['retry_flag']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
