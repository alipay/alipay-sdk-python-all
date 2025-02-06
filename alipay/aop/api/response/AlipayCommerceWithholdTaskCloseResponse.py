#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceWithholdTaskCloseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceWithholdTaskCloseResponse, self).__init__()
        self._out_trade_no = None
        self._withhold_no = None

    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def withhold_no(self):
        return self._withhold_no

    @withhold_no.setter
    def withhold_no(self, value):
        self._withhold_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceWithholdTaskCloseResponse, self).parse_response_content(response_content)
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'withhold_no' in response:
            self.withhold_no = response['withhold_no']
