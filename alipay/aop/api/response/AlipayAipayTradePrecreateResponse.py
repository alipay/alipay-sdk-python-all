#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAipayTradePrecreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAipayTradePrecreateResponse, self).__init__()
        self._out_trade_no = None
        self._pay_url = None
        self._pic_url = None

    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def pay_url(self):
        return self._pay_url

    @pay_url.setter
    def pay_url(self, value):
        self._pay_url = value
    @property
    def pic_url(self):
        return self._pic_url

    @pic_url.setter
    def pic_url(self, value):
        self._pic_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayAipayTradePrecreateResponse, self).parse_response_content(response_content)
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'pay_url' in response:
            self.pay_url = response['pay_url']
        if 'pic_url' in response:
            self.pic_url = response['pic_url']
