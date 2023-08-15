#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechMorseMarketingShopDataQueryModel(object):

    def __init__(self):
        self._account_pid = None
        self._bussiness_code = None
        self._city_name = None
        self._county_name = None
        self._latitude = None
        self._longitude = None
        self._poi_id = None
        self._province_name = None
        self._score_type = None
        self._shop_address = None
        self._shop_name = None
        self._task_id = None

    @property
    def account_pid(self):
        return self._account_pid

    @account_pid.setter
    def account_pid(self, value):
        self._account_pid = value
    @property
    def bussiness_code(self):
        return self._bussiness_code

    @bussiness_code.setter
    def bussiness_code(self, value):
        self._bussiness_code = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def county_name(self):
        return self._county_name

    @county_name.setter
    def county_name(self, value):
        self._county_name = value
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
    def poi_id(self):
        return self._poi_id

    @poi_id.setter
    def poi_id(self, value):
        self._poi_id = value
    @property
    def province_name(self):
        return self._province_name

    @province_name.setter
    def province_name(self, value):
        self._province_name = value
    @property
    def score_type(self):
        return self._score_type

    @score_type.setter
    def score_type(self, value):
        if isinstance(value, list):
            self._score_type = list()
            for i in value:
                self._score_type.append(i)
    @property
    def shop_address(self):
        return self._shop_address

    @shop_address.setter
    def shop_address(self, value):
        self._shop_address = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_pid:
            if hasattr(self.account_pid, 'to_alipay_dict'):
                params['account_pid'] = self.account_pid.to_alipay_dict()
            else:
                params['account_pid'] = self.account_pid
        if self.bussiness_code:
            if hasattr(self.bussiness_code, 'to_alipay_dict'):
                params['bussiness_code'] = self.bussiness_code.to_alipay_dict()
            else:
                params['bussiness_code'] = self.bussiness_code
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.county_name:
            if hasattr(self.county_name, 'to_alipay_dict'):
                params['county_name'] = self.county_name.to_alipay_dict()
            else:
                params['county_name'] = self.county_name
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
        if self.poi_id:
            if hasattr(self.poi_id, 'to_alipay_dict'):
                params['poi_id'] = self.poi_id.to_alipay_dict()
            else:
                params['poi_id'] = self.poi_id
        if self.province_name:
            if hasattr(self.province_name, 'to_alipay_dict'):
                params['province_name'] = self.province_name.to_alipay_dict()
            else:
                params['province_name'] = self.province_name
        if self.score_type:
            if isinstance(self.score_type, list):
                for i in range(0, len(self.score_type)):
                    element = self.score_type[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.score_type[i] = element.to_alipay_dict()
            if hasattr(self.score_type, 'to_alipay_dict'):
                params['score_type'] = self.score_type.to_alipay_dict()
            else:
                params['score_type'] = self.score_type
        if self.shop_address:
            if hasattr(self.shop_address, 'to_alipay_dict'):
                params['shop_address'] = self.shop_address.to_alipay_dict()
            else:
                params['shop_address'] = self.shop_address
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechMorseMarketingShopDataQueryModel()
        if 'account_pid' in d:
            o.account_pid = d['account_pid']
        if 'bussiness_code' in d:
            o.bussiness_code = d['bussiness_code']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'county_name' in d:
            o.county_name = d['county_name']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'poi_id' in d:
            o.poi_id = d['poi_id']
        if 'province_name' in d:
            o.province_name = d['province_name']
        if 'score_type' in d:
            o.score_type = d['score_type']
        if 'shop_address' in d:
            o.shop_address = d['shop_address']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


