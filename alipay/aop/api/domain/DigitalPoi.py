#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DigitalPoi(object):

    def __init__(self):
        self._address = None
        self._category_one = None
        self._category_two = None
        self._city_code = None
        self._district_code = None
        self._latitude = None
        self._longitude = None
        self._name = None
        self._poi_mid = None
        self._province_code = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def category_one(self):
        return self._category_one

    @category_one.setter
    def category_one(self, value):
        self._category_one = value
    @property
    def category_two(self):
        return self._category_two

    @category_two.setter
    def category_two(self, value):
        self._category_two = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
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
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def poi_mid(self):
        return self._poi_mid

    @poi_mid.setter
    def poi_mid(self, value):
        self._poi_mid = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.category_one:
            if hasattr(self.category_one, 'to_alipay_dict'):
                params['category_one'] = self.category_one.to_alipay_dict()
            else:
                params['category_one'] = self.category_one
        if self.category_two:
            if hasattr(self.category_two, 'to_alipay_dict'):
                params['category_two'] = self.category_two.to_alipay_dict()
            else:
                params['category_two'] = self.category_two
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
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
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.poi_mid:
            if hasattr(self.poi_mid, 'to_alipay_dict'):
                params['poi_mid'] = self.poi_mid.to_alipay_dict()
            else:
                params['poi_mid'] = self.poi_mid
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DigitalPoi()
        if 'address' in d:
            o.address = d['address']
        if 'category_one' in d:
            o.category_one = d['category_one']
        if 'category_two' in d:
            o.category_two = d['category_two']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'name' in d:
            o.name = d['name']
        if 'poi_mid' in d:
            o.poi_mid = d['poi_mid']
        if 'province_code' in d:
            o.province_code = d['province_code']
        return o


