#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportEtcSettlementReverseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEtcSettlementReverseResponse, self).__init__()
        self._out_order_id = None
        self._trade_status = None

    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def trade_status(self):
        return self._trade_status

    @trade_status.setter
    def trade_status(self, value):
        self._trade_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportEtcSettlementReverseResponse, self).parse_response_content(response_content)
        if 'out_order_id' in response:
            self.out_order_id = response['out_order_id']
        if 'trade_status' in response:
            self.trade_status = response['trade_status']
