#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HbMeiWeishopInfo(object):

    def __init__(self):
        self._city_code = None
        self._city_name = None
        self._logo = None
        self._pirce_per_avg_shop = None
        self._poi_name = None
        self._province_code = None
        self._province_name = None
        self._shop_gis = None
        self._shop_id = None
        self._shop_name = None
        self._star_rate_shop = None
        self._status = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def pirce_per_avg_shop(self):
        return self._pirce_per_avg_shop

    @pirce_per_avg_shop.setter
    def pirce_per_avg_shop(self, value):
        self._pirce_per_avg_shop = value
    @property
    def poi_name(self):
        return self._poi_name

    @poi_name.setter
    def poi_name(self, value):
        self._poi_name = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def province_name(self):
        return self._province_name

    @province_name.setter
    def province_name(self, value):
        self._province_name = value
    @property
    def shop_gis(self):
        return self._shop_gis

    @shop_gis.setter
    def shop_gis(self, value):
        self._shop_gis = value
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
    def star_rate_shop(self):
        return self._star_rate_shop

    @star_rate_shop.setter
    def star_rate_shop(self, value):
        self._star_rate_shop = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.pirce_per_avg_shop:
            if hasattr(self.pirce_per_avg_shop, 'to_alipay_dict'):
                params['pirce_per_avg_shop'] = self.pirce_per_avg_shop.to_alipay_dict()
            else:
                params['pirce_per_avg_shop'] = self.pirce_per_avg_shop
        if self.poi_name:
            if hasattr(self.poi_name, 'to_alipay_dict'):
                params['poi_name'] = self.poi_name.to_alipay_dict()
            else:
                params['poi_name'] = self.poi_name
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.province_name:
            if hasattr(self.province_name, 'to_alipay_dict'):
                params['province_name'] = self.province_name.to_alipay_dict()
            else:
                params['province_name'] = self.province_name
        if self.shop_gis:
            if hasattr(self.shop_gis, 'to_alipay_dict'):
                params['shop_gis'] = self.shop_gis.to_alipay_dict()
            else:
                params['shop_gis'] = self.shop_gis
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
        if self.star_rate_shop:
            if hasattr(self.star_rate_shop, 'to_alipay_dict'):
                params['star_rate_shop'] = self.star_rate_shop.to_alipay_dict()
            else:
                params['star_rate_shop'] = self.star_rate_shop
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HbMeiWeishopInfo()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'logo' in d:
            o.logo = d['logo']
        if 'pirce_per_avg_shop' in d:
            o.pirce_per_avg_shop = d['pirce_per_avg_shop']
        if 'poi_name' in d:
            o.poi_name = d['poi_name']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'province_name' in d:
            o.province_name = d['province_name']
        if 'shop_gis' in d:
            o.shop_gis = d['shop_gis']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'star_rate_shop' in d:
            o.star_rate_shop = d['star_rate_shop']
        if 'status' in d:
            o.status = d['status']
        return o


