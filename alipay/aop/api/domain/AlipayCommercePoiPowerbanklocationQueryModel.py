#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommercePoiPowerbanklocationQueryModel(object):

    def __init__(self):
        self._ext = None
        self._latitude = None
        self._longitude = None
        self._radius_range = None

    @property
    def ext(self):
        return self._ext

    @ext.setter
    def ext(self, value):
        self._ext = value
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
    def radius_range(self):
        return self._radius_range

    @radius_range.setter
    def radius_range(self, value):
        self._radius_range = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext:
            if hasattr(self.ext, 'to_alipay_dict'):
                params['ext'] = self.ext.to_alipay_dict()
            else:
                params['ext'] = self.ext
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
        if self.radius_range:
            if hasattr(self.radius_range, 'to_alipay_dict'):
                params['radius_range'] = self.radius_range.to_alipay_dict()
            else:
                params['radius_range'] = self.radius_range
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommercePoiPowerbanklocationQueryModel()
        if 'ext' in d:
            o.ext = d['ext']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'radius_range' in d:
            o.radius_range = d['radius_range']
        return o


