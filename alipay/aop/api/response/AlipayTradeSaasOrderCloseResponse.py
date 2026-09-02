#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeSaasOrderCloseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSaasOrderCloseResponse, self).__init__()
        self._close_time = None
        self._order_no = None
        self._out_trade_no = None
        self._trade_no = None
        self._trade_status = None

    @property
    def close_time(self):
        return self._close_time

    @close_time.setter
    def close_time(self, value):
        self._close_time = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
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
    @property
    def trade_status(self):
        return self._trade_status

    @trade_status.setter
    def trade_status(self, value):
        self._trade_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSaasOrderCloseResponse, self).parse_response_content(response_content)
        if 'close_time' in response:
            self.close_time = response['close_time']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
        if 'trade_status' in response:
            self.trade_status = response['trade_status']
