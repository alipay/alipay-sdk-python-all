#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EcLocationInfo(object):

    def __init__(self):
        self._address = None
        self._city_id = None
        self._city_name = None
        self._district_id = None
        self._district_name = None
        self._latitude = None
        self._longitude = None
        self._poi_id = None
        self._province_id = None
        self._province_name = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def city_id(self):
        return self._city_id

    @city_id.setter
    def city_id(self, value):
        self._city_id = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def district_id(self):
        return self._district_id

    @district_id.setter
    def district_id(self, value):
        self._district_id = value
    @property
    def district_name(self):
        return self._district_name

    @district_name.setter
    def district_name(self, value):
        self._district_name = value
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
    def poi_id(self):
        return self._poi_id

    @poi_id.setter
    def poi_id(self, value):
        self._poi_id = value
    @property
    def province_id(self):
        return self._province_id

    @province_id.setter
    def province_id(self, value):
        self._province_id = value
    @property
    def province_name(self):
        return self._province_name

    @province_name.setter
    def province_name(self, value):
        self._province_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.city_id:
            if hasattr(self.city_id, 'to_alipay_dict'):
                params['city_id'] = self.city_id.to_alipay_dict()
            else:
                params['city_id'] = self.city_id
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.district_id:
            if hasattr(self.district_id, 'to_alipay_dict'):
                params['district_id'] = self.district_id.to_alipay_dict()
            else:
                params['district_id'] = self.district_id
        if self.district_name:
            if hasattr(self.district_name, 'to_alipay_dict'):
                params['district_name'] = self.district_name.to_alipay_dict()
            else:
                params['district_name'] = self.district_name
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
        if self.poi_id:
            if hasattr(self.poi_id, 'to_alipay_dict'):
                params['poi_id'] = self.poi_id.to_alipay_dict()
            else:
                params['poi_id'] = self.poi_id
        if self.province_id:
            if hasattr(self.province_id, 'to_alipay_dict'):
                params['province_id'] = self.province_id.to_alipay_dict()
            else:
                params['province_id'] = self.province_id
        if self.province_name:
            if hasattr(self.province_name, 'to_alipay_dict'):
                params['province_name'] = self.province_name.to_alipay_dict()
            else:
                params['province_name'] = self.province_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcLocationInfo()
        if 'address' in d:
            o.address = d['address']
        if 'city_id' in d:
            o.city_id = d['city_id']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'district_id' in d:
            o.district_id = d['district_id']
        if 'district_name' in d:
            o.district_name = d['district_name']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'poi_id' in d:
            o.poi_id = d['poi_id']
        if 'province_id' in d:
            o.province_id = d['province_id']
        if 'province_name' in d:
            o.province_name = d['province_name']
        return o


