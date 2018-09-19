#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoEduKtBillingQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoEduKtBillingQueryResponse, self).__init__()
        self._order_status = None
        self._out_trade_no = None

    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoEduKtBillingQueryResponse, self).parse_response_content(response_content)
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
