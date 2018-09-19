#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarFuellingShopCreateModel(object):

    def __init__(self):
        self._address = None
        self._city_code = None
        self._district_code = None
        self._lat = None
        self._lon = None
        self._out_shop_id = None
        self._pay_url = None
        self._poi_id = None
        self._province_code = None
        self._shop_name = None
        self._shop_status = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def lat(self):
        return self._lat

    @lat.setter
    def lat(self, value):
        self._lat = value
    @property
    def lon(self):
        return self._lon

    @lon.setter
    def lon(self, value):
        self._lon = value
    @property
    def out_shop_id(self):
        return self._out_shop_id

    @out_shop_id.setter
    def out_shop_id(self, value):
        self._out_shop_id = value
    @property
    def pay_url(self):
        return self._pay_url

    @pay_url.setter
    def pay_url(self, value):
        self._pay_url = value
    @property
    def poi_id(self):
        return self._poi_id

    @poi_id.setter
    def poi_id(self, value):
        self._poi_id = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
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
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
        if self.lat:
            if hasattr(self.lat, 'to_alipay_dict'):
                params['lat'] = self.lat.to_alipay_dict()
            else:
                params['lat'] = self.lat
        if self.lon:
            if hasattr(self.lon, 'to_alipay_dict'):
                params['lon'] = self.lon.to_alipay_dict()
            else:
                params['lon'] = self.lon
        if self.out_shop_id:
            if hasattr(self.out_shop_id, 'to_alipay_dict'):
                params['out_shop_id'] = self.out_shop_id.to_alipay_dict()
            else:
                params['out_shop_id'] = self.out_shop_id
        if self.pay_url:
            if hasattr(self.pay_url, 'to_alipay_dict'):
                params['pay_url'] = self.pay_url.to_alipay_dict()
            else:
                params['pay_url'] = self.pay_url
        if self.poi_id:
            if hasattr(self.poi_id, 'to_alipay_dict'):
                params['poi_id'] = self.poi_id.to_alipay_dict()
            else:
                params['poi_id'] = self.poi_id
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
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
        o = AlipayEcoMycarFuellingShopCreateModel()
        if 'address' in d:
            o.address = d['address']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'lat' in d:
            o.lat = d['lat']
        if 'lon' in d:
            o.lon = d['lon']
        if 'out_shop_id' in d:
            o.out_shop_id = d['out_shop_id']
        if 'pay_url' in d:
            o.pay_url = d['pay_url']
        if 'poi_id' in d:
            o.poi_id = d['poi_id']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_status' in d:
            o.shop_status = d['shop_status']
        return o


