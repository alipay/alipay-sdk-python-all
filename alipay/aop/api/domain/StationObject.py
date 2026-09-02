#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StationObject(object):

    def __init__(self):
        self._metro_station_code = None
        self._metro_station_latitude = None
        self._metro_station_longitude = None
        self._metro_station_name = None

    @property
    def metro_station_code(self):
        return self._metro_station_code

    @metro_station_code.setter
    def metro_station_code(self, value):
        self._metro_station_code = value
    @property
    def metro_station_latitude(self):
        return self._metro_station_latitude

    @metro_station_latitude.setter
    def metro_station_latitude(self, value):
        self._metro_station_latitude = value
    @property
    def metro_station_longitude(self):
        return self._metro_station_longitude

    @metro_station_longitude.setter
    def metro_station_longitude(self, value):
        self._metro_station_longitude = value
    @property
    def metro_station_name(self):
        return self._metro_station_name

    @metro_station_name.setter
    def metro_station_name(self, value):
        self._metro_station_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.metro_station_code:
            if hasattr(self.metro_station_code, 'to_alipay_dict'):
                params['metro_station_code'] = self.metro_station_code.to_alipay_dict()
            else:
                params['metro_station_code'] = self.metro_station_code
        if self.metro_station_latitude:
            if hasattr(self.metro_station_latitude, 'to_alipay_dict'):
                params['metro_station_latitude'] = self.metro_station_latitude.to_alipay_dict()
            else:
                params['metro_station_latitude'] = self.metro_station_latitude
        if self.metro_station_longitude:
            if hasattr(self.metro_station_longitude, 'to_alipay_dict'):
                params['metro_station_longitude'] = self.metro_station_longitude.to_alipay_dict()
            else:
                params['metro_station_longitude'] = self.metro_station_longitude
        if self.metro_station_name:
            if hasattr(self.metro_station_name, 'to_alipay_dict'):
                params['metro_station_name'] = self.metro_station_name.to_alipay_dict()
            else:
                params['metro_station_name'] = self.metro_station_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StationObject()
        if 'metro_station_code' in d:
            o.metro_station_code = d['metro_station_code']
        if 'metro_station_latitude' in d:
            o.metro_station_latitude = d['metro_station_latitude']
        if 'metro_station_longitude' in d:
            o.metro_station_longitude = d['metro_station_longitude']
        if 'metro_station_name' in d:
            o.metro_station_name = d['metro_station_name']
        return o


