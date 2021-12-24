#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HotelInfo(object):

    def __init__(self):
        self._brand = None
        self._city = None
        self._hotel_address = None
        self._hotel_check_in_time = None
        self._hotel_check_out_time = None
        self._hotel_name = None
        self._latitude = None
        self._longitude = None
        self._province = None
        self._shop_id = None
        self._telephone = None

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def hotel_address(self):
        return self._hotel_address

    @hotel_address.setter
    def hotel_address(self, value):
        self._hotel_address = value
    @property
    def hotel_check_in_time(self):
        return self._hotel_check_in_time

    @hotel_check_in_time.setter
    def hotel_check_in_time(self, value):
        self._hotel_check_in_time = value
    @property
    def hotel_check_out_time(self):
        return self._hotel_check_out_time

    @hotel_check_out_time.setter
    def hotel_check_out_time(self, value):
        self._hotel_check_out_time = value
    @property
    def hotel_name(self):
        return self._hotel_name

    @hotel_name.setter
    def hotel_name(self, value):
        self._hotel_name = value
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
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def telephone(self):
        return self._telephone

    @telephone.setter
    def telephone(self, value):
        self._telephone = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand:
            if hasattr(self.brand, 'to_alipay_dict'):
                params['brand'] = self.brand.to_alipay_dict()
            else:
                params['brand'] = self.brand
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.hotel_address:
            if hasattr(self.hotel_address, 'to_alipay_dict'):
                params['hotel_address'] = self.hotel_address.to_alipay_dict()
            else:
                params['hotel_address'] = self.hotel_address
        if self.hotel_check_in_time:
            if hasattr(self.hotel_check_in_time, 'to_alipay_dict'):
                params['hotel_check_in_time'] = self.hotel_check_in_time.to_alipay_dict()
            else:
                params['hotel_check_in_time'] = self.hotel_check_in_time
        if self.hotel_check_out_time:
            if hasattr(self.hotel_check_out_time, 'to_alipay_dict'):
                params['hotel_check_out_time'] = self.hotel_check_out_time.to_alipay_dict()
            else:
                params['hotel_check_out_time'] = self.hotel_check_out_time
        if self.hotel_name:
            if hasattr(self.hotel_name, 'to_alipay_dict'):
                params['hotel_name'] = self.hotel_name.to_alipay_dict()
            else:
                params['hotel_name'] = self.hotel_name
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.telephone:
            if hasattr(self.telephone, 'to_alipay_dict'):
                params['telephone'] = self.telephone.to_alipay_dict()
            else:
                params['telephone'] = self.telephone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HotelInfo()
        if 'brand' in d:
            o.brand = d['brand']
        if 'city' in d:
            o.city = d['city']
        if 'hotel_address' in d:
            o.hotel_address = d['hotel_address']
        if 'hotel_check_in_time' in d:
            o.hotel_check_in_time = d['hotel_check_in_time']
        if 'hotel_check_out_time' in d:
            o.hotel_check_out_time = d['hotel_check_out_time']
        if 'hotel_name' in d:
            o.hotel_name = d['hotel_name']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'province' in d:
            o.province = d['province']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'telephone' in d:
            o.telephone = d['telephone']
        return o


