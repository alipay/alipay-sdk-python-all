#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateTradeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateTradeCreateResponse, self).__init__()
        self._edu_trade_no = None

    @property
    def edu_trade_no(self):
        return self._edu_trade_no

    @edu_trade_no.setter
    def edu_trade_no(self, value):
        self._edu_trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateTradeCreateResponse, self).parse_response_content(response_content)
        if 'edu_trade_no' in response:
            self.edu_trade_no = response['edu_trade_no']
