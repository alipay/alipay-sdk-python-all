#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserAddressInfoObj(object):

    def __init__(self):
        self._address = None
        self._address_order = None
        self._area = None
        self._city = None
        self._city_code = None
        self._floor_height = None
        self._floor_type = None
        self._house_number = None
        self._latitude = None
        self._longitude = None
        self._name = None
        self._phone = None
        self._poi_name = None
        self._province = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def address_order(self):
        return self._address_order

    @address_order.setter
    def address_order(self, value):
        self._address_order = value
    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value
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
    def floor_height(self):
        return self._floor_height

    @floor_height.setter
    def floor_height(self, value):
        self._floor_height = value
    @property
    def floor_type(self):
        return self._floor_type

    @floor_type.setter
    def floor_type(self, value):
        self._floor_type = value
    @property
    def house_number(self):
        return self._house_number

    @house_number.setter
    def house_number(self, value):
        self._house_number = value
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
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def poi_name(self):
        return self._poi_name

    @poi_name.setter
    def poi_name(self, value):
        self._poi_name = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.address_order:
            if hasattr(self.address_order, 'to_alipay_dict'):
                params['address_order'] = self.address_order.to_alipay_dict()
            else:
                params['address_order'] = self.address_order
        if self.area:
            if hasattr(self.area, 'to_alipay_dict'):
                params['area'] = self.area.to_alipay_dict()
            else:
                params['area'] = self.area
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
        if self.floor_height:
            if hasattr(self.floor_height, 'to_alipay_dict'):
                params['floor_height'] = self.floor_height.to_alipay_dict()
            else:
                params['floor_height'] = self.floor_height
        if self.floor_type:
            if hasattr(self.floor_type, 'to_alipay_dict'):
                params['floor_type'] = self.floor_type.to_alipay_dict()
            else:
                params['floor_type'] = self.floor_type
        if self.house_number:
            if hasattr(self.house_number, 'to_alipay_dict'):
                params['house_number'] = self.house_number.to_alipay_dict()
            else:
                params['house_number'] = self.house_number
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
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.poi_name:
            if hasattr(self.poi_name, 'to_alipay_dict'):
                params['poi_name'] = self.poi_name.to_alipay_dict()
            else:
                params['poi_name'] = self.poi_name
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserAddressInfoObj()
        if 'address' in d:
            o.address = d['address']
        if 'address_order' in d:
            o.address_order = d['address_order']
        if 'area' in d:
            o.area = d['area']
        if 'city' in d:
            o.city = d['city']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'floor_height' in d:
            o.floor_height = d['floor_height']
        if 'floor_type' in d:
            o.floor_type = d['floor_type']
        if 'house_number' in d:
            o.house_number = d['house_number']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'name' in d:
            o.name = d['name']
        if 'phone' in d:
            o.phone = d['phone']
        if 'poi_name' in d:
            o.poi_name = d['poi_name']
        if 'province' in d:
            o.province = d['province']
        return o


