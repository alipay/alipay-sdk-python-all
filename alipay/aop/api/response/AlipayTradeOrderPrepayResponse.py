#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.JumpInfo import JumpInfo


class AlipayTradeOrderPrepayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeOrderPrepayResponse, self).__init__()
        self._jump_info = None
        self._out_trade_no = None
        self._tn = None
        self._trade_no = None

    @property
    def jump_info(self):
        return self._jump_info

    @jump_info.setter
    def jump_info(self, value):
        if isinstance(value, JumpInfo):
            self._jump_info = value
        else:
            self._jump_info = JumpInfo.from_alipay_dict(value)
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def tn(self):
        return self._tn

    @tn.setter
    def tn(self, value):
        self._tn = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeOrderPrepayResponse, self).parse_response_content(response_content)
        if 'jump_info' in response:
            self.jump_info = response['jump_info']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'tn' in response:
            self.tn = response['tn']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
