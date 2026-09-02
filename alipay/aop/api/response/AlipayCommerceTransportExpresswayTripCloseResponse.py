#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportExpresswayTripCloseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportExpresswayTripCloseResponse, self).__init__()
        self._out_trip_id = None
        self._trade_status = None

    @property
    def out_trip_id(self):
        return self._out_trip_id

    @out_trip_id.setter
    def out_trip_id(self, value):
        self._out_trip_id = value
    @property
    def trade_status(self):
        return self._trade_status

    @trade_status.setter
    def trade_status(self, value):
        self._trade_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportExpresswayTripCloseResponse, self).parse_response_content(response_content)
        if 'out_trip_id' in response:
            self.out_trip_id = response['out_trip_id']
        if 'trade_status' in response:
            self.trade_status = response['trade_status']
