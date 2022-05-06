#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EcShopInfo(object):

    def __init__(self):
        self._address = None
        self._city_id = None
        self._city_name = None
        self._district_id = None
        self._district_name = None
        self._latitude = None
        self._longitude = None
        self._mcc_code_1 = None
        self._mcc_code_2 = None
        self._mcc_name_1 = None
        self._mcc_name_2 = None
        self._outdoor_img_url = None
        self._poi_id = None
        self._province_id = None
        self._province_name = None
        self._shop_name = None

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
    def mcc_code_1(self):
        return self._mcc_code_1

    @mcc_code_1.setter
    def mcc_code_1(self, value):
        self._mcc_code_1 = value
    @property
    def mcc_code_2(self):
        return self._mcc_code_2

    @mcc_code_2.setter
    def mcc_code_2(self, value):
        self._mcc_code_2 = value
    @property
    def mcc_name_1(self):
        return self._mcc_name_1

    @mcc_name_1.setter
    def mcc_name_1(self, value):
        self._mcc_name_1 = value
    @property
    def mcc_name_2(self):
        return self._mcc_name_2

    @mcc_name_2.setter
    def mcc_name_2(self, value):
        self._mcc_name_2 = value
    @property
    def outdoor_img_url(self):
        return self._outdoor_img_url

    @outdoor_img_url.setter
    def outdoor_img_url(self, value):
        self._outdoor_img_url = value
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
        if self.mcc_code_1:
            if hasattr(self.mcc_code_1, 'to_alipay_dict'):
                params['mcc_code_1'] = self.mcc_code_1.to_alipay_dict()
            else:
                params['mcc_code_1'] = self.mcc_code_1
        if self.mcc_code_2:
            if hasattr(self.mcc_code_2, 'to_alipay_dict'):
                params['mcc_code_2'] = self.mcc_code_2.to_alipay_dict()
            else:
                params['mcc_code_2'] = self.mcc_code_2
        if self.mcc_name_1:
            if hasattr(self.mcc_name_1, 'to_alipay_dict'):
                params['mcc_name_1'] = self.mcc_name_1.to_alipay_dict()
            else:
                params['mcc_name_1'] = self.mcc_name_1
        if self.mcc_name_2:
            if hasattr(self.mcc_name_2, 'to_alipay_dict'):
                params['mcc_name_2'] = self.mcc_name_2.to_alipay_dict()
            else:
                params['mcc_name_2'] = self.mcc_name_2
        if self.outdoor_img_url:
            if hasattr(self.outdoor_img_url, 'to_alipay_dict'):
                params['outdoor_img_url'] = self.outdoor_img_url.to_alipay_dict()
            else:
                params['outdoor_img_url'] = self.outdoor_img_url
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
        o = EcShopInfo()
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
        if 'mcc_code_1' in d:
            o.mcc_code_1 = d['mcc_code_1']
        if 'mcc_code_2' in d:
            o.mcc_code_2 = d['mcc_code_2']
        if 'mcc_name_1' in d:
            o.mcc_name_1 = d['mcc_name_1']
        if 'mcc_name_2' in d:
            o.mcc_name_2 = d['mcc_name_2']
        if 'outdoor_img_url' in d:
            o.outdoor_img_url = d['outdoor_img_url']
        if 'poi_id' in d:
            o.poi_id = d['poi_id']
        if 'province_id' in d:
            o.province_id = d['province_id']
        if 'province_name' in d:
            o.province_name = d['province_name']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        return o


