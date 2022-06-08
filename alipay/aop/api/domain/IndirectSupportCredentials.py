#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndirectSupportCredentials(object):

    def __init__(self):
        self._city = None
        self._city_code = None
        self._district = None
        self._district_code = None
        self._merchant_type = None
        self._province = None
        self._province_code = None
        self._store_address = None
        self._store_door_img = None
        self._store_inner_img = None
        self._store_name = None

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
    def merchant_type(self):
        return self._merchant_type

    @merchant_type.setter
    def merchant_type(self, value):
        self._merchant_type = value
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
    @property
    def store_address(self):
        return self._store_address

    @store_address.setter
    def store_address(self, value):
        self._store_address = value
    @property
    def store_door_img(self):
        return self._store_door_img

    @store_door_img.setter
    def store_door_img(self, value):
        self._store_door_img = value
    @property
    def store_inner_img(self):
        return self._store_inner_img

    @store_inner_img.setter
    def store_inner_img(self, value):
        self._store_inner_img = value
    @property
    def store_name(self):
        return self._store_name

    @store_name.setter
    def store_name(self, value):
        self._store_name = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.merchant_type:
            if hasattr(self.merchant_type, 'to_alipay_dict'):
                params['merchant_type'] = self.merchant_type.to_alipay_dict()
            else:
                params['merchant_type'] = self.merchant_type
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
        if self.store_address:
            if hasattr(self.store_address, 'to_alipay_dict'):
                params['store_address'] = self.store_address.to_alipay_dict()
            else:
                params['store_address'] = self.store_address
        if self.store_door_img:
            if hasattr(self.store_door_img, 'to_alipay_dict'):
                params['store_door_img'] = self.store_door_img.to_alipay_dict()
            else:
                params['store_door_img'] = self.store_door_img
        if self.store_inner_img:
            if hasattr(self.store_inner_img, 'to_alipay_dict'):
                params['store_inner_img'] = self.store_inner_img.to_alipay_dict()
            else:
                params['store_inner_img'] = self.store_inner_img
        if self.store_name:
            if hasattr(self.store_name, 'to_alipay_dict'):
                params['store_name'] = self.store_name.to_alipay_dict()
            else:
                params['store_name'] = self.store_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndirectSupportCredentials()
        if 'city' in d:
            o.city = d['city']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'district' in d:
            o.district = d['district']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'merchant_type' in d:
            o.merchant_type = d['merchant_type']
        if 'province' in d:
            o.province = d['province']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'store_address' in d:
            o.store_address = d['store_address']
        if 'store_door_img' in d:
            o.store_door_img = d['store_door_img']
        if 'store_inner_img' in d:
            o.store_inner_img = d['store_inner_img']
        if 'store_name' in d:
            o.store_name = d['store_name']
        return o


