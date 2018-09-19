#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMobilePublicGisGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMobilePublicGisGetResponse, self).__init__()
        self._accuracy = None
        self._city = None
        self._code = None
        self._latitude = None
        self._longitude = None
        self._msg = None
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
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
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
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value

    def parse_response_content(self, response_content):
        response = super(AlipayMobilePublicGisGetResponse, self).parse_response_content(response_content)
        if 'accuracy' in response:
            self.accuracy = response['accuracy']
        if 'city' in response:
            self.city = response['city']
        if 'code' in response:
            self.code = response['code']
        if 'latitude' in response:
            self.latitude = response['latitude']
        if 'longitude' in response:
            self.longitude = response['longitude']
        if 'msg' in response:
            self.msg = response['msg']
        if 'province' in response:
            self.province = response['province']
