#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SelfIndustryInfo import SelfIndustryInfo


class SelfShopGroupShopDetail(object):

    def __init__(self):
        self._address = None
        self._brand = None
        self._business_duration = None
        self._city = None
        self._district = None
        self._gmt_create = None
        self._industry_info = None
        self._label_list = None
        self._latitude = None
        self._longitude = None
        self._phone = None
        self._province = None
        self._shop_id = None
        self._shop_name = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value
    @property
    def business_duration(self):
        return self._business_duration

    @business_duration.setter
    def business_duration(self, value):
        self._business_duration = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def district(self):
        return self._district

    @district.setter
    def district(self, value):
        self._district = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def industry_info(self):
        return self._industry_info

    @industry_info.setter
    def industry_info(self, value):
        if isinstance(value, SelfIndustryInfo):
            self._industry_info = value
        else:
            self._industry_info = SelfIndustryInfo.from_alipay_dict(value)
    @property
    def label_list(self):
        return self._label_list

    @label_list.setter
    def label_list(self, value):
        if isinstance(value, list):
            self._label_list = list()
            for i in value:
                self._label_list.append(i)
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
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
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
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.brand:
            if hasattr(self.brand, 'to_alipay_dict'):
                params['brand'] = self.brand.to_alipay_dict()
            else:
                params['brand'] = self.brand
        if self.business_duration:
            if hasattr(self.business_duration, 'to_alipay_dict'):
                params['business_duration'] = self.business_duration.to_alipay_dict()
            else:
                params['business_duration'] = self.business_duration
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.district:
            if hasattr(self.district, 'to_alipay_dict'):
                params['district'] = self.district.to_alipay_dict()
            else:
                params['district'] = self.district
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.industry_info:
            if hasattr(self.industry_info, 'to_alipay_dict'):
                params['industry_info'] = self.industry_info.to_alipay_dict()
            else:
                params['industry_info'] = self.industry_info
        if self.label_list:
            if isinstance(self.label_list, list):
                for i in range(0, len(self.label_list)):
                    element = self.label_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.label_list[i] = element.to_alipay_dict()
            if hasattr(self.label_list, 'to_alipay_dict'):
                params['label_list'] = self.label_list.to_alipay_dict()
            else:
                params['label_list'] = self.label_list
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
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
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
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SelfShopGroupShopDetail()
        if 'address' in d:
            o.address = d['address']
        if 'brand' in d:
            o.brand = d['brand']
        if 'business_duration' in d:
            o.business_duration = d['business_duration']
        if 'city' in d:
            o.city = d['city']
        if 'district' in d:
            o.district = d['district']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'industry_info' in d:
            o.industry_info = d['industry_info']
        if 'label_list' in d:
            o.label_list = d['label_list']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'phone' in d:
            o.phone = d['phone']
        if 'province' in d:
            o.province = d['province']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        return o


