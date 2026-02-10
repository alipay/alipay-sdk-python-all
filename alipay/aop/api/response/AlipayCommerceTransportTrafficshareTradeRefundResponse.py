#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportTrafficshareTradeRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportTrafficshareTradeRefundResponse, self).__init__()
        self._order_no = None
        self._schedule_id = None
        self._trade_no = None

    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def schedule_id(self):
        return self._schedule_id

    @schedule_id.setter
    def schedule_id(self, value):
        self._schedule_id = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportTrafficshareTradeRefundResponse, self).parse_response_content(response_content)
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'schedule_id' in response:
            self.schedule_id = response['schedule_id']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
