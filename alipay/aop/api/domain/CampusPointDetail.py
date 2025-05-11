#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CampusPointDetail(object):

    def __init__(self):
        self._address = None
        self._aoi_id = None
        self._campus_id = None
        self._campus_name = None
        self._city = None
        self._city_code = None
        self._dist = None
        self._district = None
        self._district_code = None
        self._inst_id = None
        self._inst_name = None
        self._latitude = None
        self._longitude = None
        self._province = None
        self._province_code = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def aoi_id(self):
        return self._aoi_id

    @aoi_id.setter
    def aoi_id(self, value):
        self._aoi_id = value
    @property
    def campus_id(self):
        return self._campus_id

    @campus_id.setter
    def campus_id(self, value):
        self._campus_id = value
    @property
    def campus_name(self):
        return self._campus_name

    @campus_name.setter
    def campus_name(self, value):
        self._campus_name = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, value):
        self._dist = value
    @property
    def district(self):
        return self._district

    @district.setter
    def district(self, value):
        self._district = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def inst_name(self):
        return self._inst_name

    @inst_name.setter
    def inst_name(self, value):
        self._inst_name = value
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
        if self.aoi_id:
            if hasattr(self.aoi_id, 'to_alipay_dict'):
                params['aoi_id'] = self.aoi_id.to_alipay_dict()
            else:
                params['aoi_id'] = self.aoi_id
        if self.campus_id:
            if hasattr(self.campus_id, 'to_alipay_dict'):
                params['campus_id'] = self.campus_id.to_alipay_dict()
            else:
                params['campus_id'] = self.campus_id
        if self.campus_name:
            if hasattr(self.campus_name, 'to_alipay_dict'):
                params['campus_name'] = self.campus_name.to_alipay_dict()
            else:
                params['campus_name'] = self.campus_name
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.dist:
            if hasattr(self.dist, 'to_alipay_dict'):
                params['dist'] = self.dist.to_alipay_dict()
            else:
                params['dist'] = self.dist
        if self.district:
            if hasattr(self.district, 'to_alipay_dict'):
                params['district'] = self.district.to_alipay_dict()
            else:
                params['district'] = self.district
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.inst_name:
            if hasattr(self.inst_name, 'to_alipay_dict'):
                params['inst_name'] = self.inst_name.to_alipay_dict()
            else:
                params['inst_name'] = self.inst_name
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
        o = CampusPointDetail()
        if 'address' in d:
            o.address = d['address']
        if 'aoi_id' in d:
            o.aoi_id = d['aoi_id']
        if 'campus_id' in d:
            o.campus_id = d['campus_id']
        if 'campus_name' in d:
            o.campus_name = d['campus_name']
        if 'city' in d:
            o.city = d['city']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'dist' in d:
            o.dist = d['dist']
        if 'district' in d:
            o.district = d['district']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'inst_name' in d:
            o.inst_name = d['inst_name']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'province' in d:
            o.province = d['province']
        if 'province_code' in d:
            o.province_code = d['province_code']
        return o


