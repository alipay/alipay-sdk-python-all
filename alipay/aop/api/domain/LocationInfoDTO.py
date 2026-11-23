#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LocationInfoDTO(object):

    def __init__(self):
        self._latitude = None
        self._longitude = None
        self._up_time = None

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
    def up_time(self):
        return self._up_time

    @up_time.setter
    def up_time(self, value):
        self._up_time = value


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
        if self.up_time:
            if hasattr(self.up_time, 'to_alipay_dict'):
                params['up_time'] = self.up_time.to_alipay_dict()
            else:
                params['up_time'] = self.up_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LocationInfoDTO()
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'up_time' in d:
            o.up_time = d['up_time']
        return o


