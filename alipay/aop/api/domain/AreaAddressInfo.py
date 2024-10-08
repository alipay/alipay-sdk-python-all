#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AreaAddressInfo(object):

    def __init__(self):
        self._address = None
        self._city_code = None
        self._county_code = None
        self._gaode_poi_id = None
        self._latitude = None
        self._longitude = None
        self._province_code = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def county_code(self):
        return self._county_code

    @county_code.setter
    def county_code(self, value):
        self._county_code = value
    @property
    def gaode_poi_id(self):
        return self._gaode_poi_id

    @gaode_poi_id.setter
    def gaode_poi_id(self, value):
        self._gaode_poi_id = value
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
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.county_code:
            if hasattr(self.county_code, 'to_alipay_dict'):
                params['county_code'] = self.county_code.to_alipay_dict()
            else:
                params['county_code'] = self.county_code
        if self.gaode_poi_id:
            if hasattr(self.gaode_poi_id, 'to_alipay_dict'):
                params['gaode_poi_id'] = self.gaode_poi_id.to_alipay_dict()
            else:
                params['gaode_poi_id'] = self.gaode_poi_id
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
        o = AreaAddressInfo()
        if 'address' in d:
            o.address = d['address']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'county_code' in d:
            o.county_code = d['county_code']
        if 'gaode_poi_id' in d:
            o.gaode_poi_id = d['gaode_poi_id']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'province_code' in d:
            o.province_code = d['province_code']
        return o


