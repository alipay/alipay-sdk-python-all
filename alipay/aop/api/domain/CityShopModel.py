#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CityShopModel(object):

    def __init__(self):
        self._city_id = None
        self._city_name = None
        self._district_id = None
        self._district_name = None
        self._pos_shop = None
        self._province_id = None
        self._province_name = None
        self._shop_id = None
        self._shop_name = None
        self._shop_status = None

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
    def pos_shop(self):
        return self._pos_shop

    @pos_shop.setter
    def pos_shop(self, value):
        self._pos_shop = value
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
    @property
    def shop_status(self):
        return self._shop_status

    @shop_status.setter
    def shop_status(self, value):
        self._shop_status = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.pos_shop:
            if hasattr(self.pos_shop, 'to_alipay_dict'):
                params['pos_shop'] = self.pos_shop.to_alipay_dict()
            else:
                params['pos_shop'] = self.pos_shop
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
        if self.shop_status:
            if hasattr(self.shop_status, 'to_alipay_dict'):
                params['shop_status'] = self.shop_status.to_alipay_dict()
            else:
                params['shop_status'] = self.shop_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CityShopModel()
        if 'city_id' in d:
            o.city_id = d['city_id']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'district_id' in d:
            o.district_id = d['district_id']
        if 'district_name' in d:
            o.district_name = d['district_name']
        if 'pos_shop' in d:
            o.pos_shop = d['pos_shop']
        if 'province_id' in d:
            o.province_id = d['province_id']
        if 'province_name' in d:
            o.province_name = d['province_name']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_status' in d:
            o.shop_status = d['shop_status']
        return o


