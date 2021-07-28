#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ScenicInfo(object):

    def __init__(self):
        self._address = None
        self._city_name = None
        self._latitude = None
        self._level = None
        self._longitude = None
        self._province_name = None
        self._scenic_id = None
        self._scenic_name = None
        self._telephone = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def province_name(self):
        return self._province_name

    @province_name.setter
    def province_name(self, value):
        self._province_name = value
    @property
    def scenic_id(self):
        return self._scenic_id

    @scenic_id.setter
    def scenic_id(self, value):
        self._scenic_id = value
    @property
    def scenic_name(self):
        return self._scenic_name

    @scenic_name.setter
    def scenic_name(self, value):
        self._scenic_name = value
    @property
    def telephone(self):
        return self._telephone

    @telephone.setter
    def telephone(self, value):
        self._telephone = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = self.level.to_alipay_dict()
            else:
                params['level'] = self.level
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.province_name:
            if hasattr(self.province_name, 'to_alipay_dict'):
                params['province_name'] = self.province_name.to_alipay_dict()
            else:
                params['province_name'] = self.province_name
        if self.scenic_id:
            if hasattr(self.scenic_id, 'to_alipay_dict'):
                params['scenic_id'] = self.scenic_id.to_alipay_dict()
            else:
                params['scenic_id'] = self.scenic_id
        if self.scenic_name:
            if hasattr(self.scenic_name, 'to_alipay_dict'):
                params['scenic_name'] = self.scenic_name.to_alipay_dict()
            else:
                params['scenic_name'] = self.scenic_name
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
        o = ScenicInfo()
        if 'address' in d:
            o.address = d['address']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'level' in d:
            o.level = d['level']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'province_name' in d:
            o.province_name = d['province_name']
        if 'scenic_id' in d:
            o.scenic_id = d['scenic_id']
        if 'scenic_name' in d:
            o.scenic_name = d['scenic_name']
        if 'telephone' in d:
            o.telephone = d['telephone']
        return o


