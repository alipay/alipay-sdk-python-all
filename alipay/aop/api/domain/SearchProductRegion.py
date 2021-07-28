#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SearchProductRegion(object):

    def __init__(self):
        self._is_excluded = None
        self._latitude = None
        self._longitude = None
        self._radius = None
        self._region_code = None
        self._region_name = None
        self._region_type = None

    @property
    def is_excluded(self):
        return self._is_excluded

    @is_excluded.setter
    def is_excluded(self, value):
        self._is_excluded = value
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
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
    @property
    def region_code(self):
        return self._region_code

    @region_code.setter
    def region_code(self, value):
        self._region_code = value
    @property
    def region_name(self):
        return self._region_name

    @region_name.setter
    def region_name(self, value):
        self._region_name = value
    @property
    def region_type(self):
        return self._region_type

    @region_type.setter
    def region_type(self, value):
        self._region_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.is_excluded:
            if hasattr(self.is_excluded, 'to_alipay_dict'):
                params['is_excluded'] = self.is_excluded.to_alipay_dict()
            else:
                params['is_excluded'] = self.is_excluded
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
        if self.radius:
            if hasattr(self.radius, 'to_alipay_dict'):
                params['radius'] = self.radius.to_alipay_dict()
            else:
                params['radius'] = self.radius
        if self.region_code:
            if hasattr(self.region_code, 'to_alipay_dict'):
                params['region_code'] = self.region_code.to_alipay_dict()
            else:
                params['region_code'] = self.region_code
        if self.region_name:
            if hasattr(self.region_name, 'to_alipay_dict'):
                params['region_name'] = self.region_name.to_alipay_dict()
            else:
                params['region_name'] = self.region_name
        if self.region_type:
            if hasattr(self.region_type, 'to_alipay_dict'):
                params['region_type'] = self.region_type.to_alipay_dict()
            else:
                params['region_type'] = self.region_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SearchProductRegion()
        if 'is_excluded' in d:
            o.is_excluded = d['is_excluded']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'radius' in d:
            o.radius = d['radius']
        if 'region_code' in d:
            o.region_code = d['region_code']
        if 'region_name' in d:
            o.region_name = d['region_name']
        if 'region_type' in d:
            o.region_type = d['region_type']
        return o


