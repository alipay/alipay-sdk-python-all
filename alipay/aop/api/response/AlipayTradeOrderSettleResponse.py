#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeOrderSettleResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeOrderSettleResponse, self).__init__()
        self._trade_no = None

    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeOrderSettleResponse, self).parse_response_content(response_content)
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
