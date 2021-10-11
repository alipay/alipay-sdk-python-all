#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeOrderSettleResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeOrderSettleResponse, self).__init__()
        self._settle_no = None
        self._trade_no = None

    @property
    def settle_no(self):
        return self._settle_no

    @settle_no.setter
    def settle_no(self, value):
        self._settle_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeOrderSettleResponse, self).parse_response_content(response_content)
        if 'settle_no' in response:
            self.settle_no = response['settle_no']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
