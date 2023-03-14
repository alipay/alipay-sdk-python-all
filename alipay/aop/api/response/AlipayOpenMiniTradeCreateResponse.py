#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniTradeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniTradeCreateResponse, self).__init__()
        self._mini_trade_no = None
        self._out_trade_no = None

    @property
    def mini_trade_no(self):
        return self._mini_trade_no

    @mini_trade_no.setter
    def mini_trade_no(self, value):
        self._mini_trade_no = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniTradeCreateResponse, self).parse_response_content(response_content)
        if 'mini_trade_no' in response:
            self.mini_trade_no = response['mini_trade_no']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
