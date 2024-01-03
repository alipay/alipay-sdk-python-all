#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SportsRecordInfo(object):

    def __init__(self):
        self._calorie = None
        self._distance = None
        self._duration = None
        self._finish_time = None
        self._max_altitude = None
        self._min_altitude = None
        self._record_date = None
        self._record_id = None
        self._speed = None
        self._sport_status = None
        self._sport_type = None
        self._start_time = None
        self._step_count = None
        self._step_frequency = None
        self._step_stride = None

    @property
    def calorie(self):
        return self._calorie

    @calorie.setter
    def calorie(self, value):
        self._calorie = value
    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
    @property
    def finish_time(self):
        return self._finish_time

    @finish_time.setter
    def finish_time(self, value):
        self._finish_time = value
    @property
    def max_altitude(self):
        return self._max_altitude

    @max_altitude.setter
    def max_altitude(self, value):
        self._max_altitude = value
    @property
    def min_altitude(self):
        return self._min_altitude

    @min_altitude.setter
    def min_altitude(self, value):
        self._min_altitude = value
    @property
    def record_date(self):
        return self._record_date

    @record_date.setter
    def record_date(self, value):
        self._record_date = value
    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value
    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value
    @property
    def sport_status(self):
        return self._sport_status

    @sport_status.setter
    def sport_status(self, value):
        self._sport_status = value
    @property
    def sport_type(self):
        return self._sport_type

    @sport_type.setter
    def sport_type(self, value):
        self._sport_type = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def step_count(self):
        return self._step_count

    @step_count.setter
    def step_count(self, value):
        self._step_count = value
    @property
    def step_frequency(self):
        return self._step_frequency

    @step_frequency.setter
    def step_frequency(self, value):
        self._step_frequency = value
    @property
    def step_stride(self):
        return self._step_stride

    @step_stride.setter
    def step_stride(self, value):
        self._step_stride = value


    def to_alipay_dict(self):
        params = dict()
        if self.calorie:
            if hasattr(self.calorie, 'to_alipay_dict'):
                params['calorie'] = self.calorie.to_alipay_dict()
            else:
                params['calorie'] = self.calorie
        if self.distance:
            if hasattr(self.distance, 'to_alipay_dict'):
                params['distance'] = self.distance.to_alipay_dict()
            else:
                params['distance'] = self.distance
        if self.duration:
            if hasattr(self.duration, 'to_alipay_dict'):
                params['duration'] = self.duration.to_alipay_dict()
            else:
                params['duration'] = self.duration
        if self.finish_time:
            if hasattr(self.finish_time, 'to_alipay_dict'):
                params['finish_time'] = self.finish_time.to_alipay_dict()
            else:
                params['finish_time'] = self.finish_time
        if self.max_altitude:
            if hasattr(self.max_altitude, 'to_alipay_dict'):
                params['max_altitude'] = self.max_altitude.to_alipay_dict()
            else:
                params['max_altitude'] = self.max_altitude
        if self.min_altitude:
            if hasattr(self.min_altitude, 'to_alipay_dict'):
                params['min_altitude'] = self.min_altitude.to_alipay_dict()
            else:
                params['min_altitude'] = self.min_altitude
        if self.record_date:
            if hasattr(self.record_date, 'to_alipay_dict'):
                params['record_date'] = self.record_date.to_alipay_dict()
            else:
                params['record_date'] = self.record_date
        if self.record_id:
            if hasattr(self.record_id, 'to_alipay_dict'):
                params['record_id'] = self.record_id.to_alipay_dict()
            else:
                params['record_id'] = self.record_id
        if self.speed:
            if hasattr(self.speed, 'to_alipay_dict'):
                params['speed'] = self.speed.to_alipay_dict()
            else:
                params['speed'] = self.speed
        if self.sport_status:
            if hasattr(self.sport_status, 'to_alipay_dict'):
                params['sport_status'] = self.sport_status.to_alipay_dict()
            else:
                params['sport_status'] = self.sport_status
        if self.sport_type:
            if hasattr(self.sport_type, 'to_alipay_dict'):
                params['sport_type'] = self.sport_type.to_alipay_dict()
            else:
                params['sport_type'] = self.sport_type
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.step_count:
            if hasattr(self.step_count, 'to_alipay_dict'):
                params['step_count'] = self.step_count.to_alipay_dict()
            else:
                params['step_count'] = self.step_count
        if self.step_frequency:
            if hasattr(self.step_frequency, 'to_alipay_dict'):
                params['step_frequency'] = self.step_frequency.to_alipay_dict()
            else:
                params['step_frequency'] = self.step_frequency
        if self.step_stride:
            if hasattr(self.step_stride, 'to_alipay_dict'):
                params['step_stride'] = self.step_stride.to_alipay_dict()
            else:
                params['step_stride'] = self.step_stride
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SportsRecordInfo()
        if 'calorie' in d:
            o.calorie = d['calorie']
        if 'distance' in d:
            o.distance = d['distance']
        if 'duration' in d:
            o.duration = d['duration']
        if 'finish_time' in d:
            o.finish_time = d['finish_time']
        if 'max_altitude' in d:
            o.max_altitude = d['max_altitude']
        if 'min_altitude' in d:
            o.min_altitude = d['min_altitude']
        if 'record_date' in d:
            o.record_date = d['record_date']
        if 'record_id' in d:
            o.record_id = d['record_id']
        if 'speed' in d:
            o.speed = d['speed']
        if 'sport_status' in d:
            o.sport_status = d['sport_status']
        if 'sport_type' in d:
            o.sport_type = d['sport_type']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'step_count' in d:
            o.step_count = d['step_count']
        if 'step_frequency' in d:
            o.step_frequency = d['step_frequency']
        if 'step_stride' in d:
            o.step_stride = d['step_stride']
        return o


