#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StoreExtendInfo(object):

    def __init__(self):
        self._address = None
        self._address_ext_info = None
        self._city_name = None
        self._latitude = None
        self._longitude = None
        self._province_name = None
        self._store_id = None
        self._store_name = None
        self._telephone = None
        self._trade_id = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def address_ext_info(self):
        return self._address_ext_info

    @address_ext_info.setter
    def address_ext_info(self, value):
        self._address_ext_info = value
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
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def store_name(self):
        return self._store_name

    @store_name.setter
    def store_name(self, value):
        self._store_name = value
    @property
    def telephone(self):
        return self._telephone

    @telephone.setter
    def telephone(self, value):
        self._telephone = value
    @property
    def trade_id(self):
        return self._trade_id

    @trade_id.setter
    def trade_id(self, value):
        self._trade_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.address_ext_info:
            if hasattr(self.address_ext_info, 'to_alipay_dict'):
                params['address_ext_info'] = self.address_ext_info.to_alipay_dict()
            else:
                params['address_ext_info'] = self.address_ext_info
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
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.store_name:
            if hasattr(self.store_name, 'to_alipay_dict'):
                params['store_name'] = self.store_name.to_alipay_dict()
            else:
                params['store_name'] = self.store_name
        if self.telephone:
            if hasattr(self.telephone, 'to_alipay_dict'):
                params['telephone'] = self.telephone.to_alipay_dict()
            else:
                params['telephone'] = self.telephone
        if self.trade_id:
            if hasattr(self.trade_id, 'to_alipay_dict'):
                params['trade_id'] = self.trade_id.to_alipay_dict()
            else:
                params['trade_id'] = self.trade_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StoreExtendInfo()
        if 'address' in d:
            o.address = d['address']
        if 'address_ext_info' in d:
            o.address_ext_info = d['address_ext_info']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'province_name' in d:
            o.province_name = d['province_name']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'store_name' in d:
            o.store_name = d['store_name']
        if 'telephone' in d:
            o.telephone = d['telephone']
        if 'trade_id' in d:
            o.trade_id = d['trade_id']
        return o


