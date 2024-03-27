#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CarResponse import CarResponse


class AlipayCommerceTransportChargerPncQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportChargerPncQueryResponse, self).__init__()
        self._cars = None
        self._status = None

    @property
    def cars(self):
        return self._cars

    @cars.setter
    def cars(self, value):
        if isinstance(value, list):
            self._cars = list()
            for i in value:
                if isinstance(i, CarResponse):
                    self._cars.append(i)
                else:
                    self._cars.append(CarResponse.from_alipay_dict(i))
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportChargerPncQueryResponse, self).parse_response_content(response_content)
        if 'cars' in response:
            self.cars = response['cars']
        if 'status' in response:
            self.status = response['status']
