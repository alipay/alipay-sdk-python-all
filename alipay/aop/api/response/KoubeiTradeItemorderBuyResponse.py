#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiTradeItemorderBuyResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiTradeItemorderBuyResponse, self).__init__()
        self._cashier_order_id = None
        self._order_no = None
        self._trade_no = None

    @property
    def cashier_order_id(self):
        return self._cashier_order_id

    @cashier_order_id.setter
    def cashier_order_id(self, value):
        self._cashier_order_id = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(KoubeiTradeItemorderBuyResponse, self).parse_response_content(response_content)
        if 'cashier_order_id' in response:
            self.cashier_order_id = response['cashier_order_id']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
