#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SingleTripDurationQueryOpenapiResult(object):

    def __init__(self):
        self._direction = None
        self._end_time = None
        self._ext_info = None
        self._line_id = None
        self._line_key = None
        self._single_trip_duration = None
        self._start_time = None

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def line_id(self):
        return self._line_id

    @line_id.setter
    def line_id(self, value):
        self._line_id = value
    @property
    def line_key(self):
        return self._line_key

    @line_key.setter
    def line_key(self, value):
        self._line_key = value
    @property
    def single_trip_duration(self):
        return self._single_trip_duration

    @single_trip_duration.setter
    def single_trip_duration(self, value):
        self._single_trip_duration = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.direction:
            if hasattr(self.direction, 'to_alipay_dict'):
                params['direction'] = self.direction.to_alipay_dict()
            else:
                params['direction'] = self.direction
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.line_id:
            if hasattr(self.line_id, 'to_alipay_dict'):
                params['line_id'] = self.line_id.to_alipay_dict()
            else:
                params['line_id'] = self.line_id
        if self.line_key:
            if hasattr(self.line_key, 'to_alipay_dict'):
                params['line_key'] = self.line_key.to_alipay_dict()
            else:
                params['line_key'] = self.line_key
        if self.single_trip_duration:
            if hasattr(self.single_trip_duration, 'to_alipay_dict'):
                params['single_trip_duration'] = self.single_trip_duration.to_alipay_dict()
            else:
                params['single_trip_duration'] = self.single_trip_duration
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
        o = SingleTripDurationQueryOpenapiResult()
        if 'direction' in d:
            o.direction = d['direction']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'line_id' in d:
            o.line_id = d['line_id']
        if 'line_key' in d:
            o.line_key = d['line_key']
        if 'single_trip_duration' in d:
            o.single_trip_duration = d['single_trip_duration']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


