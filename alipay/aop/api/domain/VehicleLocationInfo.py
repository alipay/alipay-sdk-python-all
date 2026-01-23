#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VehicleLocationInfo(object):

    def __init__(self):
        self._car_code = None
        self._car_level = None
        self._lat = None
        self._lon = None
        self._vehicle_license = None
        self._vehicle_model_id = None

    @property
    def car_code(self):
        return self._car_code

    @car_code.setter
    def car_code(self, value):
        self._car_code = value
    @property
    def car_level(self):
        return self._car_level

    @car_level.setter
    def car_level(self, value):
        self._car_level = value
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
    def vehicle_license(self):
        return self._vehicle_license

    @vehicle_license.setter
    def vehicle_license(self, value):
        self._vehicle_license = value
    @property
    def vehicle_model_id(self):
        return self._vehicle_model_id

    @vehicle_model_id.setter
    def vehicle_model_id(self, value):
        self._vehicle_model_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.car_code:
            if hasattr(self.car_code, 'to_alipay_dict'):
                params['car_code'] = self.car_code.to_alipay_dict()
            else:
                params['car_code'] = self.car_code
        if self.car_level:
            if hasattr(self.car_level, 'to_alipay_dict'):
                params['car_level'] = self.car_level.to_alipay_dict()
            else:
                params['car_level'] = self.car_level
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
        if self.vehicle_license:
            if hasattr(self.vehicle_license, 'to_alipay_dict'):
                params['vehicle_license'] = self.vehicle_license.to_alipay_dict()
            else:
                params['vehicle_license'] = self.vehicle_license
        if self.vehicle_model_id:
            if hasattr(self.vehicle_model_id, 'to_alipay_dict'):
                params['vehicle_model_id'] = self.vehicle_model_id.to_alipay_dict()
            else:
                params['vehicle_model_id'] = self.vehicle_model_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VehicleLocationInfo()
        if 'car_code' in d:
            o.car_code = d['car_code']
        if 'car_level' in d:
            o.car_level = d['car_level']
        if 'lat' in d:
            o.lat = d['lat']
        if 'lon' in d:
            o.lon = d['lon']
        if 'vehicle_license' in d:
            o.vehicle_license = d['vehicle_license']
        if 'vehicle_model_id' in d:
            o.vehicle_model_id = d['vehicle_model_id']
        return o


