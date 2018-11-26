#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeCancelResponse, self).__init__()
        self._action = None
        self._gmt_refund_pay = None
        self._out_trade_no = None
        self._refund_settlement_id = None
        self._retry_flag = None
        self._trade_no = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def gmt_refund_pay(self):
        return self._gmt_refund_pay

    @gmt_refund_pay.setter
    def gmt_refund_pay(self, value):
        self._gmt_refund_pay = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def refund_settlement_id(self):
        return self._refund_settlement_id

    @refund_settlement_id.setter
    def refund_settlement_id(self, value):
        self._refund_settlement_id = value
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
        response = super(AlipayTradeCancelResponse, self).parse_response_content(response_content)
        if 'action' in response:
            self.action = response['action']
        if 'gmt_refund_pay' in response:
            self.gmt_refund_pay = response['gmt_refund_pay']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'refund_settlement_id' in response:
            self.refund_settlement_id = response['refund_settlement_id']
        if 'retry_flag' in response:
            self.retry_flag = response['retry_flag']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
