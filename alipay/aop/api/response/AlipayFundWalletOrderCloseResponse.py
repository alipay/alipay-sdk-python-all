#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundWalletOrderCloseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundWalletOrderCloseResponse, self).__init__()
        self._close_order = None
        self._fund_order_id = None

    @property
    def close_order(self):
        return self._close_order

    @close_order.setter
    def close_order(self, value):
        self._close_order = value
    @property
    def fund_order_id(self):
        return self._fund_order_id

    @fund_order_id.setter
    def fund_order_id(self, value):
        self._fund_order_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundWalletOrderCloseResponse, self).parse_response_content(response_content)
        if 'close_order' in response:
            self.close_order = response['close_order']
        if 'fund_order_id' in response:
            self.fund_order_id = response['fund_order_id']
