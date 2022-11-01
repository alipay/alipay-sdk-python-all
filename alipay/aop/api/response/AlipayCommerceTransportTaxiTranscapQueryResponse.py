#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PositionPoint import PositionPoint


class AlipayCommerceTransportTaxiTranscapQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportTaxiTranscapQueryResponse, self).__init__()
        self._car_no = None
        self._positions = None
        self._vehicle_id = None

    @property
    def car_no(self):
        return self._car_no

    @car_no.setter
    def car_no(self, value):
        self._car_no = value
    @property
    def positions(self):
        return self._positions

    @positions.setter
    def positions(self, value):
        if isinstance(value, list):
            self._positions = list()
            for i in value:
                if isinstance(i, PositionPoint):
                    self._positions.append(i)
                else:
                    self._positions.append(PositionPoint.from_alipay_dict(i))
    @property
    def vehicle_id(self):
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, value):
        self._vehicle_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportTaxiTranscapQueryResponse, self).parse_response_content(response_content)
        if 'car_no' in response:
            self.car_no = response['car_no']
        if 'positions' in response:
            self.positions = response['positions']
        if 'vehicle_id' in response:
            self.vehicle_id = response['vehicle_id']
