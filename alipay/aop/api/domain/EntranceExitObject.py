#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EntranceExitObject(object):

    def __init__(self):
        self._entrance_exit_code = None
        self._entrance_exit_latitude = None
        self._entrance_exit_longitude = None
        self._entrance_exit_name = None
        self._metro_station_code = None

    @property
    def entrance_exit_code(self):
        return self._entrance_exit_code

    @entrance_exit_code.setter
    def entrance_exit_code(self, value):
        self._entrance_exit_code = value
    @property
    def entrance_exit_latitude(self):
        return self._entrance_exit_latitude

    @entrance_exit_latitude.setter
    def entrance_exit_latitude(self, value):
        self._entrance_exit_latitude = value
    @property
    def entrance_exit_longitude(self):
        return self._entrance_exit_longitude

    @entrance_exit_longitude.setter
    def entrance_exit_longitude(self, value):
        self._entrance_exit_longitude = value
    @property
    def entrance_exit_name(self):
        return self._entrance_exit_name

    @entrance_exit_name.setter
    def entrance_exit_name(self, value):
        self._entrance_exit_name = value
    @property
    def metro_station_code(self):
        return self._metro_station_code

    @metro_station_code.setter
    def metro_station_code(self, value):
        self._metro_station_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.entrance_exit_code:
            if hasattr(self.entrance_exit_code, 'to_alipay_dict'):
                params['entrance_exit_code'] = self.entrance_exit_code.to_alipay_dict()
            else:
                params['entrance_exit_code'] = self.entrance_exit_code
        if self.entrance_exit_latitude:
            if hasattr(self.entrance_exit_latitude, 'to_alipay_dict'):
                params['entrance_exit_latitude'] = self.entrance_exit_latitude.to_alipay_dict()
            else:
                params['entrance_exit_latitude'] = self.entrance_exit_latitude
        if self.entrance_exit_longitude:
            if hasattr(self.entrance_exit_longitude, 'to_alipay_dict'):
                params['entrance_exit_longitude'] = self.entrance_exit_longitude.to_alipay_dict()
            else:
                params['entrance_exit_longitude'] = self.entrance_exit_longitude
        if self.entrance_exit_name:
            if hasattr(self.entrance_exit_name, 'to_alipay_dict'):
                params['entrance_exit_name'] = self.entrance_exit_name.to_alipay_dict()
            else:
                params['entrance_exit_name'] = self.entrance_exit_name
        if self.metro_station_code:
            if hasattr(self.metro_station_code, 'to_alipay_dict'):
                params['metro_station_code'] = self.metro_station_code.to_alipay_dict()
            else:
                params['metro_station_code'] = self.metro_station_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EntranceExitObject()
        if 'entrance_exit_code' in d:
            o.entrance_exit_code = d['entrance_exit_code']
        if 'entrance_exit_latitude' in d:
            o.entrance_exit_latitude = d['entrance_exit_latitude']
        if 'entrance_exit_longitude' in d:
            o.entrance_exit_longitude = d['entrance_exit_longitude']
        if 'entrance_exit_name' in d:
            o.entrance_exit_name = d['entrance_exit_name']
        if 'metro_station_code' in d:
            o.metro_station_code = d['metro_station_code']
        return o


