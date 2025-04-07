#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudpromoBoardingpointInfoSyncModel(object):

    def __init__(self):
        self._boarding_point_name = None
        self._comfort_level = None
        self._floor = None
        self._latitude = None
        self._longitude = None
        self._place_name = None
        self._poi_id = None
        self._vehicle_type = None
        self._wait_people_number = None
        self._wait_time = None

    @property
    def boarding_point_name(self):
        return self._boarding_point_name

    @boarding_point_name.setter
    def boarding_point_name(self, value):
        self._boarding_point_name = value
    @property
    def comfort_level(self):
        return self._comfort_level

    @comfort_level.setter
    def comfort_level(self, value):
        self._comfort_level = value
    @property
    def floor(self):
        return self._floor

    @floor.setter
    def floor(self, value):
        self._floor = value
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
    def place_name(self):
        return self._place_name

    @place_name.setter
    def place_name(self, value):
        self._place_name = value
    @property
    def poi_id(self):
        return self._poi_id

    @poi_id.setter
    def poi_id(self, value):
        self._poi_id = value
    @property
    def vehicle_type(self):
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, value):
        self._vehicle_type = value
    @property
    def wait_people_number(self):
        return self._wait_people_number

    @wait_people_number.setter
    def wait_people_number(self, value):
        self._wait_people_number = value
    @property
    def wait_time(self):
        return self._wait_time

    @wait_time.setter
    def wait_time(self, value):
        self._wait_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.boarding_point_name:
            if hasattr(self.boarding_point_name, 'to_alipay_dict'):
                params['boarding_point_name'] = self.boarding_point_name.to_alipay_dict()
            else:
                params['boarding_point_name'] = self.boarding_point_name
        if self.comfort_level:
            if hasattr(self.comfort_level, 'to_alipay_dict'):
                params['comfort_level'] = self.comfort_level.to_alipay_dict()
            else:
                params['comfort_level'] = self.comfort_level
        if self.floor:
            if hasattr(self.floor, 'to_alipay_dict'):
                params['floor'] = self.floor.to_alipay_dict()
            else:
                params['floor'] = self.floor
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
        if self.place_name:
            if hasattr(self.place_name, 'to_alipay_dict'):
                params['place_name'] = self.place_name.to_alipay_dict()
            else:
                params['place_name'] = self.place_name
        if self.poi_id:
            if hasattr(self.poi_id, 'to_alipay_dict'):
                params['poi_id'] = self.poi_id.to_alipay_dict()
            else:
                params['poi_id'] = self.poi_id
        if self.vehicle_type:
            if hasattr(self.vehicle_type, 'to_alipay_dict'):
                params['vehicle_type'] = self.vehicle_type.to_alipay_dict()
            else:
                params['vehicle_type'] = self.vehicle_type
        if self.wait_people_number:
            if hasattr(self.wait_people_number, 'to_alipay_dict'):
                params['wait_people_number'] = self.wait_people_number.to_alipay_dict()
            else:
                params['wait_people_number'] = self.wait_people_number
        if self.wait_time:
            if hasattr(self.wait_time, 'to_alipay_dict'):
                params['wait_time'] = self.wait_time.to_alipay_dict()
            else:
                params['wait_time'] = self.wait_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoBoardingpointInfoSyncModel()
        if 'boarding_point_name' in d:
            o.boarding_point_name = d['boarding_point_name']
        if 'comfort_level' in d:
            o.comfort_level = d['comfort_level']
        if 'floor' in d:
            o.floor = d['floor']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'place_name' in d:
            o.place_name = d['place_name']
        if 'poi_id' in d:
            o.poi_id = d['poi_id']
        if 'vehicle_type' in d:
            o.vehicle_type = d['vehicle_type']
        if 'wait_people_number' in d:
            o.wait_people_number = d['wait_people_number']
        if 'wait_time' in d:
            o.wait_time = d['wait_time']
        return o


