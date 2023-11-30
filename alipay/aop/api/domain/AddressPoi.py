#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AddressPoi(object):

    def __init__(self):
        self._county_code = None
        self._lat = None
        self._lon = None
        self._name = None
        self._poi_id = None

    @property
    def county_code(self):
        return self._county_code

    @county_code.setter
    def county_code(self, value):
        self._county_code = value
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
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def poi_id(self):
        return self._poi_id

    @poi_id.setter
    def poi_id(self, value):
        self._poi_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.county_code:
            if hasattr(self.county_code, 'to_alipay_dict'):
                params['county_code'] = self.county_code.to_alipay_dict()
            else:
                params['county_code'] = self.county_code
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
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.poi_id:
            if hasattr(self.poi_id, 'to_alipay_dict'):
                params['poi_id'] = self.poi_id.to_alipay_dict()
            else:
                params['poi_id'] = self.poi_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AddressPoi()
        if 'county_code' in d:
            o.county_code = d['county_code']
        if 'lat' in d:
            o.lat = d['lat']
        if 'lon' in d:
            o.lon = d['lon']
        if 'name' in d:
            o.name = d['name']
        if 'poi_id' in d:
            o.poi_id = d['poi_id']
        return o


