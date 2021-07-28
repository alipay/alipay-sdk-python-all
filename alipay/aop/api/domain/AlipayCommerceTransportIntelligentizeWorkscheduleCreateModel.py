#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RestTime import RestTime
from alipay.aop.api.domain.WorkPattern import WorkPattern


class AlipayCommerceTransportIntelligentizeWorkscheduleCreateModel(object):

    def __init__(self):
        self._city_code = None
        self._corp_id = None
        self._down_first_station_capacity = None
        self._ext_param = None
        self._line_key = None
        self._request_id = None
        self._rest_time_list = None
        self._service_task_name = None
        self._timetable_direction = None
        self._trip_break_time = None
        self._up_first_station_capacity = None
        self._work_pattern_list = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def corp_id(self):
        return self._corp_id

    @corp_id.setter
    def corp_id(self, value):
        self._corp_id = value
    @property
    def down_first_station_capacity(self):
        return self._down_first_station_capacity

    @down_first_station_capacity.setter
    def down_first_station_capacity(self, value):
        self._down_first_station_capacity = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def line_key(self):
        return self._line_key

    @line_key.setter
    def line_key(self, value):
        self._line_key = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def rest_time_list(self):
        return self._rest_time_list

    @rest_time_list.setter
    def rest_time_list(self, value):
        if isinstance(value, list):
            self._rest_time_list = list()
            for i in value:
                if isinstance(i, RestTime):
                    self._rest_time_list.append(i)
                else:
                    self._rest_time_list.append(RestTime.from_alipay_dict(i))
    @property
    def service_task_name(self):
        return self._service_task_name

    @service_task_name.setter
    def service_task_name(self, value):
        self._service_task_name = value
    @property
    def timetable_direction(self):
        return self._timetable_direction

    @timetable_direction.setter
    def timetable_direction(self, value):
        self._timetable_direction = value
    @property
    def trip_break_time(self):
        return self._trip_break_time

    @trip_break_time.setter
    def trip_break_time(self, value):
        self._trip_break_time = value
    @property
    def up_first_station_capacity(self):
        return self._up_first_station_capacity

    @up_first_station_capacity.setter
    def up_first_station_capacity(self, value):
        self._up_first_station_capacity = value
    @property
    def work_pattern_list(self):
        return self._work_pattern_list

    @work_pattern_list.setter
    def work_pattern_list(self, value):
        if isinstance(value, list):
            self._work_pattern_list = list()
            for i in value:
                if isinstance(i, WorkPattern):
                    self._work_pattern_list.append(i)
                else:
                    self._work_pattern_list.append(WorkPattern.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.corp_id:
            if hasattr(self.corp_id, 'to_alipay_dict'):
                params['corp_id'] = self.corp_id.to_alipay_dict()
            else:
                params['corp_id'] = self.corp_id
        if self.down_first_station_capacity:
            if hasattr(self.down_first_station_capacity, 'to_alipay_dict'):
                params['down_first_station_capacity'] = self.down_first_station_capacity.to_alipay_dict()
            else:
                params['down_first_station_capacity'] = self.down_first_station_capacity
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.line_key:
            if hasattr(self.line_key, 'to_alipay_dict'):
                params['line_key'] = self.line_key.to_alipay_dict()
            else:
                params['line_key'] = self.line_key
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.rest_time_list:
            if isinstance(self.rest_time_list, list):
                for i in range(0, len(self.rest_time_list)):
                    element = self.rest_time_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rest_time_list[i] = element.to_alipay_dict()
            if hasattr(self.rest_time_list, 'to_alipay_dict'):
                params['rest_time_list'] = self.rest_time_list.to_alipay_dict()
            else:
                params['rest_time_list'] = self.rest_time_list
        if self.service_task_name:
            if hasattr(self.service_task_name, 'to_alipay_dict'):
                params['service_task_name'] = self.service_task_name.to_alipay_dict()
            else:
                params['service_task_name'] = self.service_task_name
        if self.timetable_direction:
            if hasattr(self.timetable_direction, 'to_alipay_dict'):
                params['timetable_direction'] = self.timetable_direction.to_alipay_dict()
            else:
                params['timetable_direction'] = self.timetable_direction
        if self.trip_break_time:
            if hasattr(self.trip_break_time, 'to_alipay_dict'):
                params['trip_break_time'] = self.trip_break_time.to_alipay_dict()
            else:
                params['trip_break_time'] = self.trip_break_time
        if self.up_first_station_capacity:
            if hasattr(self.up_first_station_capacity, 'to_alipay_dict'):
                params['up_first_station_capacity'] = self.up_first_station_capacity.to_alipay_dict()
            else:
                params['up_first_station_capacity'] = self.up_first_station_capacity
        if self.work_pattern_list:
            if isinstance(self.work_pattern_list, list):
                for i in range(0, len(self.work_pattern_list)):
                    element = self.work_pattern_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.work_pattern_list[i] = element.to_alipay_dict()
            if hasattr(self.work_pattern_list, 'to_alipay_dict'):
                params['work_pattern_list'] = self.work_pattern_list.to_alipay_dict()
            else:
                params['work_pattern_list'] = self.work_pattern_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportIntelligentizeWorkscheduleCreateModel()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'corp_id' in d:
            o.corp_id = d['corp_id']
        if 'down_first_station_capacity' in d:
            o.down_first_station_capacity = d['down_first_station_capacity']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'line_key' in d:
            o.line_key = d['line_key']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'rest_time_list' in d:
            o.rest_time_list = d['rest_time_list']
        if 'service_task_name' in d:
            o.service_task_name = d['service_task_name']
        if 'timetable_direction' in d:
            o.timetable_direction = d['timetable_direction']
        if 'trip_break_time' in d:
            o.trip_break_time = d['trip_break_time']
        if 'up_first_station_capacity' in d:
            o.up_first_station_capacity = d['up_first_station_capacity']
        if 'work_pattern_list' in d:
            o.work_pattern_list = d['work_pattern_list']
        return o


