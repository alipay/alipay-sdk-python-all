#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeSubscriptionPayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSubscriptionPayResponse, self).__init__()
        self._order_no = None
        self._out_trade_no = None
        self._status = None
        self._subscription_id = None
        self._trade_no = None

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
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def subscription_id(self):
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self._subscription_id = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSubscriptionPayResponse, self).parse_response_content(response_content)
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'status' in response:
            self.status = response['status']
        if 'subscription_id' in response:
            self.subscription_id = response['subscription_id']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
