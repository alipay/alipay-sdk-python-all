#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMapGeocodingReverseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMapGeocodingReverseResponse, self).__init__()
        self._city = None
        self._district = None
        self._province = None

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def district(self):
        return self._district

    @district.setter
    def district(self, value):
        self._district = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMapGeocodingReverseResponse, self).parse_response_content(response_content)
        if 'city' in response:
            self.city = response['city']
        if 'district' in response:
            self.district = response['district']
        if 'province' in response:
            self.province = response['province']
