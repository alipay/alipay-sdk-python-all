#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportParkingFeeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportParkingFeeQueryResponse, self).__init__()
        self._charging_rule_img_url = None
        self._charging_rule_text = None
        self._discount_info = None
        self._gaode_map_poi = None
        self._gaode_map_poi_latitude = None
        self._gaode_map_poi_longitude = None
        self._in_place_time = None
        self._park_duration_time = None
        self._parking_lot_address = None
        self._parking_lot_name = None
        self._pay_url = None
        self._total_amount = None

    @property
    def charging_rule_img_url(self):
        return self._charging_rule_img_url

    @charging_rule_img_url.setter
    def charging_rule_img_url(self, value):
        self._charging_rule_img_url = value
    @property
    def charging_rule_text(self):
        return self._charging_rule_text

    @charging_rule_text.setter
    def charging_rule_text(self, value):
        self._charging_rule_text = value
    @property
    def discount_info(self):
        return self._discount_info

    @discount_info.setter
    def discount_info(self, value):
        self._discount_info = value
    @property
    def gaode_map_poi(self):
        return self._gaode_map_poi

    @gaode_map_poi.setter
    def gaode_map_poi(self, value):
        self._gaode_map_poi = value
    @property
    def gaode_map_poi_latitude(self):
        return self._gaode_map_poi_latitude

    @gaode_map_poi_latitude.setter
    def gaode_map_poi_latitude(self, value):
        self._gaode_map_poi_latitude = value
    @property
    def gaode_map_poi_longitude(self):
        return self._gaode_map_poi_longitude

    @gaode_map_poi_longitude.setter
    def gaode_map_poi_longitude(self, value):
        self._gaode_map_poi_longitude = value
    @property
    def in_place_time(self):
        return self._in_place_time

    @in_place_time.setter
    def in_place_time(self, value):
        self._in_place_time = value
    @property
    def park_duration_time(self):
        return self._park_duration_time

    @park_duration_time.setter
    def park_duration_time(self, value):
        self._park_duration_time = value
    @property
    def parking_lot_address(self):
        return self._parking_lot_address

    @parking_lot_address.setter
    def parking_lot_address(self, value):
        self._parking_lot_address = value
    @property
    def parking_lot_name(self):
        return self._parking_lot_name

    @parking_lot_name.setter
    def parking_lot_name(self, value):
        self._parking_lot_name = value
    @property
    def pay_url(self):
        return self._pay_url

    @pay_url.setter
    def pay_url(self, value):
        self._pay_url = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportParkingFeeQueryResponse, self).parse_response_content(response_content)
        if 'charging_rule_img_url' in response:
            self.charging_rule_img_url = response['charging_rule_img_url']
        if 'charging_rule_text' in response:
            self.charging_rule_text = response['charging_rule_text']
        if 'discount_info' in response:
            self.discount_info = response['discount_info']
        if 'gaode_map_poi' in response:
            self.gaode_map_poi = response['gaode_map_poi']
        if 'gaode_map_poi_latitude' in response:
            self.gaode_map_poi_latitude = response['gaode_map_poi_latitude']
        if 'gaode_map_poi_longitude' in response:
            self.gaode_map_poi_longitude = response['gaode_map_poi_longitude']
        if 'in_place_time' in response:
            self.in_place_time = response['in_place_time']
        if 'park_duration_time' in response:
            self.park_duration_time = response['park_duration_time']
        if 'parking_lot_address' in response:
            self.parking_lot_address = response['parking_lot_address']
        if 'parking_lot_name' in response:
            self.parking_lot_name = response['parking_lot_name']
        if 'pay_url' in response:
            self.pay_url = response['pay_url']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
