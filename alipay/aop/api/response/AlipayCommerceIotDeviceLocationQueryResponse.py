#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotDeviceLocationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotDeviceLocationQueryResponse, self).__init__()
        self._latitude = None
        self._longitude = None
        self._time = None

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotDeviceLocationQueryResponse, self).parse_response_content(response_content)
        if 'latitude' in response:
            self.latitude = response['latitude']
        if 'longitude' in response:
            self.longitude = response['longitude']
        if 'time' in response:
            self.time = response['time']
