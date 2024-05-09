#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AdressInfo(object):

    def __init__(self):
        self._city_id = None
        self._district_id = None
        self._poi_id = None
        self._province_id = None

    @property
    def city_id(self):
        return self._city_id

    @city_id.setter
    def city_id(self, value):
        self._city_id = value
    @property
    def district_id(self):
        return self._district_id

    @district_id.setter
    def district_id(self, value):
        self._district_id = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.city_id:
            if hasattr(self.city_id, 'to_alipay_dict'):
                params['city_id'] = self.city_id.to_alipay_dict()
            else:
                params['city_id'] = self.city_id
        if self.district_id:
            if hasattr(self.district_id, 'to_alipay_dict'):
                params['district_id'] = self.district_id.to_alipay_dict()
            else:
                params['district_id'] = self.district_id
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AdressInfo()
        if 'city_id' in d:
            o.city_id = d['city_id']
        if 'district_id' in d:
            o.district_id = d['district_id']
        if 'poi_id' in d:
            o.poi_id = d['poi_id']
        if 'province_id' in d:
            o.province_id = d['province_id']
        return o


