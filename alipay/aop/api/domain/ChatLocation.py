#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChatLocation(object):

    def __init__(self):
        self._latitude = None
        self._longitude = None
        self._poi_name = None
        self._poi_type = None

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
    def poi_name(self):
        return self._poi_name

    @poi_name.setter
    def poi_name(self, value):
        self._poi_name = value
    @property
    def poi_type(self):
        return self._poi_type

    @poi_type.setter
    def poi_type(self, value):
        self._poi_type = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.poi_name:
            if hasattr(self.poi_name, 'to_alipay_dict'):
                params['poi_name'] = self.poi_name.to_alipay_dict()
            else:
                params['poi_name'] = self.poi_name
        if self.poi_type:
            if hasattr(self.poi_type, 'to_alipay_dict'):
                params['poi_type'] = self.poi_type.to_alipay_dict()
            else:
                params['poi_type'] = self.poi_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChatLocation()
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'poi_name' in d:
            o.poi_name = d['poi_name']
        if 'poi_type' in d:
            o.poi_type = d['poi_type']
        return o


