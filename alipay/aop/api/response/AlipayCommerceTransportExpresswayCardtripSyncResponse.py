#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportExpresswayCardtripSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportExpresswayCardtripSyncResponse, self).__init__()
        self._out_trip_id = None
        self._trip_id = None

    @property
    def out_trip_id(self):
        return self._out_trip_id

    @out_trip_id.setter
    def out_trip_id(self, value):
        self._out_trip_id = value
    @property
    def trip_id(self):
        return self._trip_id

    @trip_id.setter
    def trip_id(self, value):
        self._trip_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportExpresswayCardtripSyncResponse, self).parse_response_content(response_content)
        if 'out_trip_id' in response:
            self.out_trip_id = response['out_trip_id']
        if 'trip_id' in response:
            self.trip_id = response['trip_id']
