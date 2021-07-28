#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommercePoiPowerbanklocationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommercePoiPowerbanklocationQueryResponse, self).__init__()
        self._address_desc = None
        self._applet_link = None
        self._brand_name = None
        self._distance = None
        self._exist = None
        self._h_five_link = None
        self._interface_type = None
        self._latitude = None
        self._longitude = None
        self._price = None
        self._zfb_text_content = None

    @property
    def address_desc(self):
        return self._address_desc

    @address_desc.setter
    def address_desc(self, value):
        self._address_desc = value
    @property
    def applet_link(self):
        return self._applet_link

    @applet_link.setter
    def applet_link(self, value):
        self._applet_link = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value
    @property
    def exist(self):
        return self._exist

    @exist.setter
    def exist(self, value):
        self._exist = value
    @property
    def h_five_link(self):
        return self._h_five_link

    @h_five_link.setter
    def h_five_link(self, value):
        self._h_five_link = value
    @property
    def interface_type(self):
        return self._interface_type

    @interface_type.setter
    def interface_type(self, value):
        self._interface_type = value
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
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def zfb_text_content(self):
        return self._zfb_text_content

    @zfb_text_content.setter
    def zfb_text_content(self, value):
        self._zfb_text_content = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommercePoiPowerbanklocationQueryResponse, self).parse_response_content(response_content)
        if 'address_desc' in response:
            self.address_desc = response['address_desc']
        if 'applet_link' in response:
            self.applet_link = response['applet_link']
        if 'brand_name' in response:
            self.brand_name = response['brand_name']
        if 'distance' in response:
            self.distance = response['distance']
        if 'exist' in response:
            self.exist = response['exist']
        if 'h_five_link' in response:
            self.h_five_link = response['h_five_link']
        if 'interface_type' in response:
            self.interface_type = response['interface_type']
        if 'latitude' in response:
            self.latitude = response['latitude']
        if 'longitude' in response:
            self.longitude = response['longitude']
        if 'price' in response:
            self.price = response['price']
        if 'zfb_text_content' in response:
            self.zfb_text_content = response['zfb_text_content']
