#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TimeInterval import TimeInterval


class TimeTableLineInfo(object):

    def __init__(self):
        self._customized_time_interval_list = None
        self._direction = None
        self._expect_trip_count = None
        self._ext_param = None
        self._line_id = None
        self._line_key = None
        self._max_time_interval = None
        self._min_time_interval = None
        self._service_end_time = None
        self._service_start_time = None
        self._time_span = None
        self._vehicle_capacity = None

    @property
    def customized_time_interval_list(self):
        return self._customized_time_interval_list

    @customized_time_interval_list.setter
    def customized_time_interval_list(self, value):
        if isinstance(value, list):
            self._customized_time_interval_list = list()
            for i in value:
                if isinstance(i, TimeInterval):
                    self._customized_time_interval_list.append(i)
                else:
                    self._customized_time_interval_list.append(TimeInterval.from_alipay_dict(i))
    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value
    @property
    def expect_trip_count(self):
        return self._expect_trip_count

    @expect_trip_count.setter
    def expect_trip_count(self, value):
        self._expect_trip_count = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
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
    def max_time_interval(self):
        return self._max_time_interval

    @max_time_interval.setter
    def max_time_interval(self, value):
        self._max_time_interval = value
    @property
    def min_time_interval(self):
        return self._min_time_interval

    @min_time_interval.setter
    def min_time_interval(self, value):
        self._min_time_interval = value
    @property
    def service_end_time(self):
        return self._service_end_time

    @service_end_time.setter
    def service_end_time(self, value):
        self._service_end_time = value
    @property
    def service_start_time(self):
        return self._service_start_time

    @service_start_time.setter
    def service_start_time(self, value):
        self._service_start_time = value
    @property
    def time_span(self):
        return self._time_span

    @time_span.setter
    def time_span(self, value):
        self._time_span = value
    @property
    def vehicle_capacity(self):
        return self._vehicle_capacity

    @vehicle_capacity.setter
    def vehicle_capacity(self, value):
        self._vehicle_capacity = value


    def to_alipay_dict(self):
        params = dict()
        if self.customized_time_interval_list:
            if isinstance(self.customized_time_interval_list, list):
                for i in range(0, len(self.customized_time_interval_list)):
                    element = self.customized_time_interval_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.customized_time_interval_list[i] = element.to_alipay_dict()
            if hasattr(self.customized_time_interval_list, 'to_alipay_dict'):
                params['customized_time_interval_list'] = self.customized_time_interval_list.to_alipay_dict()
            else:
                params['customized_time_interval_list'] = self.customized_time_interval_list
        if self.direction:
            if hasattr(self.direction, 'to_alipay_dict'):
                params['direction'] = self.direction.to_alipay_dict()
            else:
                params['direction'] = self.direction
        if self.expect_trip_count:
            if hasattr(self.expect_trip_count, 'to_alipay_dict'):
                params['expect_trip_count'] = self.expect_trip_count.to_alipay_dict()
            else:
                params['expect_trip_count'] = self.expect_trip_count
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
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
        if self.max_time_interval:
            if hasattr(self.max_time_interval, 'to_alipay_dict'):
                params['max_time_interval'] = self.max_time_interval.to_alipay_dict()
            else:
                params['max_time_interval'] = self.max_time_interval
        if self.min_time_interval:
            if hasattr(self.min_time_interval, 'to_alipay_dict'):
                params['min_time_interval'] = self.min_time_interval.to_alipay_dict()
            else:
                params['min_time_interval'] = self.min_time_interval
        if self.service_end_time:
            if hasattr(self.service_end_time, 'to_alipay_dict'):
                params['service_end_time'] = self.service_end_time.to_alipay_dict()
            else:
                params['service_end_time'] = self.service_end_time
        if self.service_start_time:
            if hasattr(self.service_start_time, 'to_alipay_dict'):
                params['service_start_time'] = self.service_start_time.to_alipay_dict()
            else:
                params['service_start_time'] = self.service_start_time
        if self.time_span:
            if hasattr(self.time_span, 'to_alipay_dict'):
                params['time_span'] = self.time_span.to_alipay_dict()
            else:
                params['time_span'] = self.time_span
        if self.vehicle_capacity:
            if hasattr(self.vehicle_capacity, 'to_alipay_dict'):
                params['vehicle_capacity'] = self.vehicle_capacity.to_alipay_dict()
            else:
                params['vehicle_capacity'] = self.vehicle_capacity
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TimeTableLineInfo()
        if 'customized_time_interval_list' in d:
            o.customized_time_interval_list = d['customized_time_interval_list']
        if 'direction' in d:
            o.direction = d['direction']
        if 'expect_trip_count' in d:
            o.expect_trip_count = d['expect_trip_count']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'line_id' in d:
            o.line_id = d['line_id']
        if 'line_key' in d:
            o.line_key = d['line_key']
        if 'max_time_interval' in d:
            o.max_time_interval = d['max_time_interval']
        if 'min_time_interval' in d:
            o.min_time_interval = d['min_time_interval']
        if 'service_end_time' in d:
            o.service_end_time = d['service_end_time']
        if 'service_start_time' in d:
            o.service_start_time = d['service_start_time']
        if 'time_span' in d:
            o.time_span = d['time_span']
        if 'vehicle_capacity' in d:
            o.vehicle_capacity = d['vehicle_capacity']
        return o


