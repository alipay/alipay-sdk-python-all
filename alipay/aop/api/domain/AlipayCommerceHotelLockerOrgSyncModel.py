#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceHotelLockerOrgSyncModel(object):

    def __init__(self):
        self._alipay_org_id = None
        self._area = None
        self._area_code = None
        self._brand = None
        self._city = None
        self._city_code = None
        self._isv_org_id = None
        self._latitude = None
        self._longitude = None
        self._memo = None
        self._merchant_id = None
        self._operators_code = None
        self._org_address = None
        self._org_group_code = None
        self._org_name = None
        self._province = None
        self._province_code = None
        self._scene_type = None
        self._shop_id = None
        self._telephone = None

    @property
    def alipay_org_id(self):
        return self._alipay_org_id

    @alipay_org_id.setter
    def alipay_org_id(self, value):
        self._alipay_org_id = value
    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value
    @property
    def area_code(self):
        return self._area_code

    @area_code.setter
    def area_code(self, value):
        self._area_code = value
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
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def isv_org_id(self):
        return self._isv_org_id

    @isv_org_id.setter
    def isv_org_id(self, value):
        self._isv_org_id = value
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
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def operators_code(self):
        return self._operators_code

    @operators_code.setter
    def operators_code(self, value):
        self._operators_code = value
    @property
    def org_address(self):
        return self._org_address

    @org_address.setter
    def org_address(self, value):
        self._org_address = value
    @property
    def org_group_code(self):
        return self._org_group_code

    @org_group_code.setter
    def org_group_code(self, value):
        self._org_group_code = value
    @property
    def org_name(self):
        return self._org_name

    @org_name.setter
    def org_name(self, value):
        self._org_name = value
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
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value
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
        if self.alipay_org_id:
            if hasattr(self.alipay_org_id, 'to_alipay_dict'):
                params['alipay_org_id'] = self.alipay_org_id.to_alipay_dict()
            else:
                params['alipay_org_id'] = self.alipay_org_id
        if self.area:
            if hasattr(self.area, 'to_alipay_dict'):
                params['area'] = self.area.to_alipay_dict()
            else:
                params['area'] = self.area
        if self.area_code:
            if hasattr(self.area_code, 'to_alipay_dict'):
                params['area_code'] = self.area_code.to_alipay_dict()
            else:
                params['area_code'] = self.area_code
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
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.isv_org_id:
            if hasattr(self.isv_org_id, 'to_alipay_dict'):
                params['isv_org_id'] = self.isv_org_id.to_alipay_dict()
            else:
                params['isv_org_id'] = self.isv_org_id
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
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.operators_code:
            if hasattr(self.operators_code, 'to_alipay_dict'):
                params['operators_code'] = self.operators_code.to_alipay_dict()
            else:
                params['operators_code'] = self.operators_code
        if self.org_address:
            if hasattr(self.org_address, 'to_alipay_dict'):
                params['org_address'] = self.org_address.to_alipay_dict()
            else:
                params['org_address'] = self.org_address
        if self.org_group_code:
            if hasattr(self.org_group_code, 'to_alipay_dict'):
                params['org_group_code'] = self.org_group_code.to_alipay_dict()
            else:
                params['org_group_code'] = self.org_group_code
        if self.org_name:
            if hasattr(self.org_name, 'to_alipay_dict'):
                params['org_name'] = self.org_name.to_alipay_dict()
            else:
                params['org_name'] = self.org_name
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
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
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
        o = AlipayCommerceHotelLockerOrgSyncModel()
        if 'alipay_org_id' in d:
            o.alipay_org_id = d['alipay_org_id']
        if 'area' in d:
            o.area = d['area']
        if 'area_code' in d:
            o.area_code = d['area_code']
        if 'brand' in d:
            o.brand = d['brand']
        if 'city' in d:
            o.city = d['city']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'isv_org_id' in d:
            o.isv_org_id = d['isv_org_id']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'memo' in d:
            o.memo = d['memo']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'operators_code' in d:
            o.operators_code = d['operators_code']
        if 'org_address' in d:
            o.org_address = d['org_address']
        if 'org_group_code' in d:
            o.org_group_code = d['org_group_code']
        if 'org_name' in d:
            o.org_name = d['org_name']
        if 'province' in d:
            o.province = d['province']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'telephone' in d:
            o.telephone = d['telephone']
        return o


