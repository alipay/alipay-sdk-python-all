#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CalendarInfoDTO import CalendarInfoDTO


class ScheduleInfoDTO(object):

    def __init__(self):
        self._begin_time = None
        self._calendar_info = None
        self._end_time = None
        self._interval = None
        self._point_time = None
        self._schedule_type = None

    @property
    def begin_time(self):
        return self._begin_time

    @begin_time.setter
    def begin_time(self, value):
        self._begin_time = value
    @property
    def calendar_info(self):
        return self._calendar_info

    @calendar_info.setter
    def calendar_info(self, value):
        if isinstance(value, CalendarInfoDTO):
            self._calendar_info = value
        else:
            self._calendar_info = CalendarInfoDTO.from_alipay_dict(value)
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def interval(self):
        return self._interval

    @interval.setter
    def interval(self, value):
        self._interval = value
    @property
    def point_time(self):
        return self._point_time

    @point_time.setter
    def point_time(self, value):
        self._point_time = value
    @property
    def schedule_type(self):
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, value):
        self._schedule_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.begin_time:
            if hasattr(self.begin_time, 'to_alipay_dict'):
                params['begin_time'] = self.begin_time.to_alipay_dict()
            else:
                params['begin_time'] = self.begin_time
        if self.calendar_info:
            if hasattr(self.calendar_info, 'to_alipay_dict'):
                params['calendar_info'] = self.calendar_info.to_alipay_dict()
            else:
                params['calendar_info'] = self.calendar_info
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.interval:
            if hasattr(self.interval, 'to_alipay_dict'):
                params['interval'] = self.interval.to_alipay_dict()
            else:
                params['interval'] = self.interval
        if self.point_time:
            if hasattr(self.point_time, 'to_alipay_dict'):
                params['point_time'] = self.point_time.to_alipay_dict()
            else:
                params['point_time'] = self.point_time
        if self.schedule_type:
            if hasattr(self.schedule_type, 'to_alipay_dict'):
                params['schedule_type'] = self.schedule_type.to_alipay_dict()
            else:
                params['schedule_type'] = self.schedule_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ScheduleInfoDTO()
        if 'begin_time' in d:
            o.begin_time = d['begin_time']
        if 'calendar_info' in d:
            o.calendar_info = d['calendar_info']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'interval' in d:
            o.interval = d['interval']
        if 'point_time' in d:
            o.point_time = d['point_time']
        if 'schedule_type' in d:
            o.schedule_type = d['schedule_type']
        return o


