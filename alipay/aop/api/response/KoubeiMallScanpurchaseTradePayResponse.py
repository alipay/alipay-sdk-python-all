#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMallScanpurchaseTradePayResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMallScanpurchaseTradePayResponse, self).__init__()
        self._cashier_id = None
        self._order_id = None
        self._trade_no = None

    @property
    def cashier_id(self):
        return self._cashier_id

    @cashier_id.setter
    def cashier_id(self, value):
        self._cashier_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMallScanpurchaseTradePayResponse, self).parse_response_content(response_content)
        if 'cashier_id' in response:
            self.cashier_id = response['cashier_id']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
