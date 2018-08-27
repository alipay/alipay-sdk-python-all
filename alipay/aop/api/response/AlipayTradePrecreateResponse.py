#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradePrecreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradePrecreateResponse, self).__init__()
        self._out_trade_no = None
        self._qr_code = None

    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def qr_code(self):
        return self._qr_code

    @qr_code.setter
    def qr_code(self, value):
        self._qr_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradePrecreateResponse, self).parse_response_content(response_content)
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'qr_code' in response:
            self.qr_code = response['qr_code']
