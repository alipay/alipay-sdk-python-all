#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OrderBuyResponse import OrderBuyResponse


class AlipayOpenMiniOrderBuyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniOrderBuyResponse, self).__init__()
        self._merge_trade_no = None
        self._mini_trade_create_responses = None
        self._trade_no_biz_type = None

    @property
    def merge_trade_no(self):
        return self._merge_trade_no

    @merge_trade_no.setter
    def merge_trade_no(self, value):
        self._merge_trade_no = value
    @property
    def mini_trade_create_responses(self):
        return self._mini_trade_create_responses

    @mini_trade_create_responses.setter
    def mini_trade_create_responses(self, value):
        if isinstance(value, list):
            self._mini_trade_create_responses = list()
            for i in value:
                if isinstance(i, OrderBuyResponse):
                    self._mini_trade_create_responses.append(i)
                else:
                    self._mini_trade_create_responses.append(OrderBuyResponse.from_alipay_dict(i))
    @property
    def trade_no_biz_type(self):
        return self._trade_no_biz_type

    @trade_no_biz_type.setter
    def trade_no_biz_type(self, value):
        self._trade_no_biz_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniOrderBuyResponse, self).parse_response_content(response_content)
        if 'merge_trade_no' in response:
            self.merge_trade_no = response['merge_trade_no']
        if 'mini_trade_create_responses' in response:
            self.mini_trade_create_responses = response['mini_trade_create_responses']
        if 'trade_no_biz_type' in response:
            self.trade_no_biz_type = response['trade_no_biz_type']
