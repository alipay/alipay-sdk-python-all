#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportTaxiTripUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportTaxiTripUploadResponse, self).__init__()
        self._trip_id = None

    @property
    def trip_id(self):
        return self._trip_id

    @trip_id.setter
    def trip_id(self, value):
        self._trip_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportTaxiTripUploadResponse, self).parse_response_content(response_content)
        if 'trip_id' in response:
            self.trip_id = response['trip_id']
