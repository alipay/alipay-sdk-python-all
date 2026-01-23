#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LocationData(object):

    def __init__(self):
        self._crowding_level = None
        self._location_id = None
        self._location_name = None
        self._location_type = None
        self._max_capacity = None
        self._visitor_day_count = None
        self._visitor_real_count = None
        self._visitor_real_time = None

    @property
    def crowding_level(self):
        return self._crowding_level

    @crowding_level.setter
    def crowding_level(self, value):
        self._crowding_level = value
    @property
    def location_id(self):
        return self._location_id

    @location_id.setter
    def location_id(self, value):
        self._location_id = value
    @property
    def location_name(self):
        return self._location_name

    @location_name.setter
    def location_name(self, value):
        self._location_name = value
    @property
    def location_type(self):
        return self._location_type

    @location_type.setter
    def location_type(self, value):
        self._location_type = value
    @property
    def max_capacity(self):
        return self._max_capacity

    @max_capacity.setter
    def max_capacity(self, value):
        self._max_capacity = value
    @property
    def visitor_day_count(self):
        return self._visitor_day_count

    @visitor_day_count.setter
    def visitor_day_count(self, value):
        self._visitor_day_count = value
    @property
    def visitor_real_count(self):
        return self._visitor_real_count

    @visitor_real_count.setter
    def visitor_real_count(self, value):
        self._visitor_real_count = value
    @property
    def visitor_real_time(self):
        return self._visitor_real_time

    @visitor_real_time.setter
    def visitor_real_time(self, value):
        self._visitor_real_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.crowding_level:
            if hasattr(self.crowding_level, 'to_alipay_dict'):
                params['crowding_level'] = self.crowding_level.to_alipay_dict()
            else:
                params['crowding_level'] = self.crowding_level
        if self.location_id:
            if hasattr(self.location_id, 'to_alipay_dict'):
                params['location_id'] = self.location_id.to_alipay_dict()
            else:
                params['location_id'] = self.location_id
        if self.location_name:
            if hasattr(self.location_name, 'to_alipay_dict'):
                params['location_name'] = self.location_name.to_alipay_dict()
            else:
                params['location_name'] = self.location_name
        if self.location_type:
            if hasattr(self.location_type, 'to_alipay_dict'):
                params['location_type'] = self.location_type.to_alipay_dict()
            else:
                params['location_type'] = self.location_type
        if self.max_capacity:
            if hasattr(self.max_capacity, 'to_alipay_dict'):
                params['max_capacity'] = self.max_capacity.to_alipay_dict()
            else:
                params['max_capacity'] = self.max_capacity
        if self.visitor_day_count:
            if hasattr(self.visitor_day_count, 'to_alipay_dict'):
                params['visitor_day_count'] = self.visitor_day_count.to_alipay_dict()
            else:
                params['visitor_day_count'] = self.visitor_day_count
        if self.visitor_real_count:
            if hasattr(self.visitor_real_count, 'to_alipay_dict'):
                params['visitor_real_count'] = self.visitor_real_count.to_alipay_dict()
            else:
                params['visitor_real_count'] = self.visitor_real_count
        if self.visitor_real_time:
            if hasattr(self.visitor_real_time, 'to_alipay_dict'):
                params['visitor_real_time'] = self.visitor_real_time.to_alipay_dict()
            else:
                params['visitor_real_time'] = self.visitor_real_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LocationData()
        if 'crowding_level' in d:
            o.crowding_level = d['crowding_level']
        if 'location_id' in d:
            o.location_id = d['location_id']
        if 'location_name' in d:
            o.location_name = d['location_name']
        if 'location_type' in d:
            o.location_type = d['location_type']
        if 'max_capacity' in d:
            o.max_capacity = d['max_capacity']
        if 'visitor_day_count' in d:
            o.visitor_day_count = d['visitor_day_count']
        if 'visitor_real_count' in d:
            o.visitor_real_count = d['visitor_real_count']
        if 'visitor_real_time' in d:
            o.visitor_real_time = d['visitor_real_time']
        return o


