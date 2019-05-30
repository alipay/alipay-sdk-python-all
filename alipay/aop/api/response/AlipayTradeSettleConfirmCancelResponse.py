#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeSettleConfirmCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSettleConfirmCancelResponse, self).__init__()
        self._ori_request_no = None
        self._trade_no = None

    @property
    def ori_request_no(self):
        return self._ori_request_no

    @ori_request_no.setter
    def ori_request_no(self, value):
        self._ori_request_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSettleConfirmCancelResponse, self).parse_response_content(response_content)
        if 'ori_request_no' in response:
            self.ori_request_no = response['ori_request_no']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
