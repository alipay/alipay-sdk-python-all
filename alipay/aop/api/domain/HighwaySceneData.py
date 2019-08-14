#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HighwaySceneData(object):

    def __init__(self):
        self._car_type = None
        self._end_province_code = None
        self._end_station_code = None
        self._end_station_id = None
        self._end_station_latitude = None
        self._end_station_longitude = None
        self._end_station_name = None
        self._end_station_province = None
        self._end_time = None
        self._lane_no = None
        self._start_province_code = None
        self._start_station_code = None
        self._start_station_id = None
        self._start_station_latitude = None
        self._start_station_longitude = None
        self._start_station_name = None
        self._start_station_province = None
        self._start_time = None

    @property
    def car_type(self):
        return self._car_type

    @car_type.setter
    def car_type(self, value):
        self._car_type = value
    @property
    def end_province_code(self):
        return self._end_province_code

    @end_province_code.setter
    def end_province_code(self, value):
        self._end_province_code = value
    @property
    def end_station_code(self):
        return self._end_station_code

    @end_station_code.setter
    def end_station_code(self, value):
        self._end_station_code = value
    @property
    def end_station_id(self):
        return self._end_station_id

    @end_station_id.setter
    def end_station_id(self, value):
        self._end_station_id = value
    @property
    def end_station_latitude(self):
        return self._end_station_latitude

    @end_station_latitude.setter
    def end_station_latitude(self, value):
        self._end_station_latitude = value
    @property
    def end_station_longitude(self):
        return self._end_station_longitude

    @end_station_longitude.setter
    def end_station_longitude(self, value):
        self._end_station_longitude = value
    @property
    def end_station_name(self):
        return self._end_station_name

    @end_station_name.setter
    def end_station_name(self, value):
        self._end_station_name = value
    @property
    def end_station_province(self):
        return self._end_station_province

    @end_station_province.setter
    def end_station_province(self, value):
        self._end_station_province = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def lane_no(self):
        return self._lane_no

    @lane_no.setter
    def lane_no(self, value):
        self._lane_no = value
    @property
    def start_province_code(self):
        return self._start_province_code

    @start_province_code.setter
    def start_province_code(self, value):
        self._start_province_code = value
    @property
    def start_station_code(self):
        return self._start_station_code

    @start_station_code.setter
    def start_station_code(self, value):
        self._start_station_code = value
    @property
    def start_station_id(self):
        return self._start_station_id

    @start_station_id.setter
    def start_station_id(self, value):
        self._start_station_id = value
    @property
    def start_station_latitude(self):
        return self._start_station_latitude

    @start_station_latitude.setter
    def start_station_latitude(self, value):
        self._start_station_latitude = value
    @property
    def start_station_longitude(self):
        return self._start_station_longitude

    @start_station_longitude.setter
    def start_station_longitude(self, value):
        self._start_station_longitude = value
    @property
    def start_station_name(self):
        return self._start_station_name

    @start_station_name.setter
    def start_station_name(self, value):
        self._start_station_name = value
    @property
    def start_station_province(self):
        return self._start_station_province

    @start_station_province.setter
    def start_station_province(self, value):
        self._start_station_province = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.car_type:
            if hasattr(self.car_type, 'to_alipay_dict'):
                params['car_type'] = self.car_type.to_alipay_dict()
            else:
                params['car_type'] = self.car_type
        if self.end_province_code:
            if hasattr(self.end_province_code, 'to_alipay_dict'):
                params['end_province_code'] = self.end_province_code.to_alipay_dict()
            else:
                params['end_province_code'] = self.end_province_code
        if self.end_station_code:
            if hasattr(self.end_station_code, 'to_alipay_dict'):
                params['end_station_code'] = self.end_station_code.to_alipay_dict()
            else:
                params['end_station_code'] = self.end_station_code
        if self.end_station_id:
            if hasattr(self.end_station_id, 'to_alipay_dict'):
                params['end_station_id'] = self.end_station_id.to_alipay_dict()
            else:
                params['end_station_id'] = self.end_station_id
        if self.end_station_latitude:
            if hasattr(self.end_station_latitude, 'to_alipay_dict'):
                params['end_station_latitude'] = self.end_station_latitude.to_alipay_dict()
            else:
                params['end_station_latitude'] = self.end_station_latitude
        if self.end_station_longitude:
            if hasattr(self.end_station_longitude, 'to_alipay_dict'):
                params['end_station_longitude'] = self.end_station_longitude.to_alipay_dict()
            else:
                params['end_station_longitude'] = self.end_station_longitude
        if self.end_station_name:
            if hasattr(self.end_station_name, 'to_alipay_dict'):
                params['end_station_name'] = self.end_station_name.to_alipay_dict()
            else:
                params['end_station_name'] = self.end_station_name
        if self.end_station_province:
            if hasattr(self.end_station_province, 'to_alipay_dict'):
                params['end_station_province'] = self.end_station_province.to_alipay_dict()
            else:
                params['end_station_province'] = self.end_station_province
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.lane_no:
            if hasattr(self.lane_no, 'to_alipay_dict'):
                params['lane_no'] = self.lane_no.to_alipay_dict()
            else:
                params['lane_no'] = self.lane_no
        if self.start_province_code:
            if hasattr(self.start_province_code, 'to_alipay_dict'):
                params['start_province_code'] = self.start_province_code.to_alipay_dict()
            else:
                params['start_province_code'] = self.start_province_code
        if self.start_station_code:
            if hasattr(self.start_station_code, 'to_alipay_dict'):
                params['start_station_code'] = self.start_station_code.to_alipay_dict()
            else:
                params['start_station_code'] = self.start_station_code
        if self.start_station_id:
            if hasattr(self.start_station_id, 'to_alipay_dict'):
                params['start_station_id'] = self.start_station_id.to_alipay_dict()
            else:
                params['start_station_id'] = self.start_station_id
        if self.start_station_latitude:
            if hasattr(self.start_station_latitude, 'to_alipay_dict'):
                params['start_station_latitude'] = self.start_station_latitude.to_alipay_dict()
            else:
                params['start_station_latitude'] = self.start_station_latitude
        if self.start_station_longitude:
            if hasattr(self.start_station_longitude, 'to_alipay_dict'):
                params['start_station_longitude'] = self.start_station_longitude.to_alipay_dict()
            else:
                params['start_station_longitude'] = self.start_station_longitude
        if self.start_station_name:
            if hasattr(self.start_station_name, 'to_alipay_dict'):
                params['start_station_name'] = self.start_station_name.to_alipay_dict()
            else:
                params['start_station_name'] = self.start_station_name
        if self.start_station_province:
            if hasattr(self.start_station_province, 'to_alipay_dict'):
                params['start_station_province'] = self.start_station_province.to_alipay_dict()
            else:
                params['start_station_province'] = self.start_station_province
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HighwaySceneData()
        if 'car_type' in d:
            o.car_type = d['car_type']
        if 'end_province_code' in d:
            o.end_province_code = d['end_province_code']
        if 'end_station_code' in d:
            o.end_station_code = d['end_station_code']
        if 'end_station_id' in d:
            o.end_station_id = d['end_station_id']
        if 'end_station_latitude' in d:
            o.end_station_latitude = d['end_station_latitude']
        if 'end_station_longitude' in d:
            o.end_station_longitude = d['end_station_longitude']
        if 'end_station_name' in d:
            o.end_station_name = d['end_station_name']
        if 'end_station_province' in d:
            o.end_station_province = d['end_station_province']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'lane_no' in d:
            o.lane_no = d['lane_no']
        if 'start_province_code' in d:
            o.start_province_code = d['start_province_code']
        if 'start_station_code' in d:
            o.start_station_code = d['start_station_code']
        if 'start_station_id' in d:
            o.start_station_id = d['start_station_id']
        if 'start_station_latitude' in d:
            o.start_station_latitude = d['start_station_latitude']
        if 'start_station_longitude' in d:
            o.start_station_longitude = d['start_station_longitude']
        if 'start_station_name' in d:
            o.start_station_name = d['start_station_name']
        if 'start_station_province' in d:
            o.start_station_province = d['start_station_province']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


