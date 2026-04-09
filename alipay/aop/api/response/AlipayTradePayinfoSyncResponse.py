#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradePayinfoSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradePayinfoSyncResponse, self).__init__()
        self._out_trade_no = None

    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradePayinfoSyncResponse, self).parse_response_content(response_content)
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
