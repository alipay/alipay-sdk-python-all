#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApprovalItinerary(object):

    def __init__(self):
        self._arr_city = None
        self._arr_city_code = None
        self._dep_city = None
        self._dep_city_code = None
        self._end_time = None
        self._itinerary_id = None
        self._start_time = None
        self._traffic_type = None
        self._trip_way = None

    @property
    def arr_city(self):
        return self._arr_city

    @arr_city.setter
    def arr_city(self, value):
        self._arr_city = value
    @property
    def arr_city_code(self):
        return self._arr_city_code

    @arr_city_code.setter
    def arr_city_code(self, value):
        self._arr_city_code = value
    @property
    def dep_city(self):
        return self._dep_city

    @dep_city.setter
    def dep_city(self, value):
        self._dep_city = value
    @property
    def dep_city_code(self):
        return self._dep_city_code

    @dep_city_code.setter
    def dep_city_code(self, value):
        self._dep_city_code = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def itinerary_id(self):
        return self._itinerary_id

    @itinerary_id.setter
    def itinerary_id(self, value):
        self._itinerary_id = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def traffic_type(self):
        return self._traffic_type

    @traffic_type.setter
    def traffic_type(self, value):
        self._traffic_type = value
    @property
    def trip_way(self):
        return self._trip_way

    @trip_way.setter
    def trip_way(self, value):
        self._trip_way = value


    def to_alipay_dict(self):
        params = dict()
        if self.arr_city:
            if hasattr(self.arr_city, 'to_alipay_dict'):
                params['arr_city'] = self.arr_city.to_alipay_dict()
            else:
                params['arr_city'] = self.arr_city
        if self.arr_city_code:
            if hasattr(self.arr_city_code, 'to_alipay_dict'):
                params['arr_city_code'] = self.arr_city_code.to_alipay_dict()
            else:
                params['arr_city_code'] = self.arr_city_code
        if self.dep_city:
            if hasattr(self.dep_city, 'to_alipay_dict'):
                params['dep_city'] = self.dep_city.to_alipay_dict()
            else:
                params['dep_city'] = self.dep_city
        if self.dep_city_code:
            if hasattr(self.dep_city_code, 'to_alipay_dict'):
                params['dep_city_code'] = self.dep_city_code.to_alipay_dict()
            else:
                params['dep_city_code'] = self.dep_city_code
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.itinerary_id:
            if hasattr(self.itinerary_id, 'to_alipay_dict'):
                params['itinerary_id'] = self.itinerary_id.to_alipay_dict()
            else:
                params['itinerary_id'] = self.itinerary_id
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.traffic_type:
            if hasattr(self.traffic_type, 'to_alipay_dict'):
                params['traffic_type'] = self.traffic_type.to_alipay_dict()
            else:
                params['traffic_type'] = self.traffic_type
        if self.trip_way:
            if hasattr(self.trip_way, 'to_alipay_dict'):
                params['trip_way'] = self.trip_way.to_alipay_dict()
            else:
                params['trip_way'] = self.trip_way
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApprovalItinerary()
        if 'arr_city' in d:
            o.arr_city = d['arr_city']
        if 'arr_city_code' in d:
            o.arr_city_code = d['arr_city_code']
        if 'dep_city' in d:
            o.dep_city = d['dep_city']
        if 'dep_city_code' in d:
            o.dep_city_code = d['dep_city_code']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'itinerary_id' in d:
            o.itinerary_id = d['itinerary_id']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'traffic_type' in d:
            o.traffic_type = d['traffic_type']
        if 'trip_way' in d:
            o.trip_way = d['trip_way']
        return o


