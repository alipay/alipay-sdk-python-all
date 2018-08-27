#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarParkingVehicleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarParkingVehicleQueryResponse, self).__init__()
        self._car_number = None

    @property
    def car_number(self):
        return self._car_number

    @car_number.setter
    def car_number(self, value):
        self._car_number = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarParkingVehicleQueryResponse, self).parse_response_content(response_content)
        if 'car_number' in response:
            self.car_number = response['car_number']
