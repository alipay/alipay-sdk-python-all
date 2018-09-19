#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicGisQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicGisQueryResponse, self).__init__()
        self._accuracy = None
        self._city = None
        self._latitude = None
        self._longitude = None
        self._province = None

    @property
    def accuracy(self):
        return self._accuracy

    @accuracy.setter
    def accuracy(self, value):
        self._accuracy = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
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
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicGisQueryResponse, self).parse_response_content(response_content)
        if 'accuracy' in response:
            self.accuracy = response['accuracy']
        if 'city' in response:
            self.city = response['city']
        if 'latitude' in response:
            self.latitude = response['latitude']
        if 'longitude' in response:
            self.longitude = response['longitude']
        if 'province' in response:
            self.province = response['province']
