#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotDeviceAddressQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotDeviceAddressQueryResponse, self).__init__()
        self._city_name = None
        self._country_name = None
        self._county_name = None
        self._province_name = None
        self._town_name = None

    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def country_name(self):
        return self._country_name

    @country_name.setter
    def country_name(self, value):
        self._country_name = value
    @property
    def county_name(self):
        return self._county_name

    @county_name.setter
    def county_name(self, value):
        self._county_name = value
    @property
    def province_name(self):
        return self._province_name

    @province_name.setter
    def province_name(self, value):
        self._province_name = value
    @property
    def town_name(self):
        return self._town_name

    @town_name.setter
    def town_name(self, value):
        self._town_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotDeviceAddressQueryResponse, self).parse_response_content(response_content)
        if 'city_name' in response:
            self.city_name = response['city_name']
        if 'country_name' in response:
            self.country_name = response['country_name']
        if 'county_name' in response:
            self.county_name = response['county_name']
        if 'province_name' in response:
            self.province_name = response['province_name']
        if 'town_name' in response:
            self.town_name = response['town_name']
