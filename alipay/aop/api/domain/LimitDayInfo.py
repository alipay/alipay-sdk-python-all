#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LimitDayInfo(object):

    def __init__(self):
        self._days_of_week = None
        self._end_time = None
        self._end_time_type = None
        self._start_time = None

    @property
    def days_of_week(self):
        return self._days_of_week

    @days_of_week.setter
    def days_of_week(self, value):
        if isinstance(value, list):
            self._days_of_week = list()
            for i in value:
                self._days_of_week.append(i)
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def end_time_type(self):
        return self._end_time_type

    @end_time_type.setter
    def end_time_type(self, value):
        self._end_time_type = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.days_of_week:
            if isinstance(self.days_of_week, list):
                for i in range(0, len(self.days_of_week)):
                    element = self.days_of_week[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.days_of_week[i] = element.to_alipay_dict()
            if hasattr(self.days_of_week, 'to_alipay_dict'):
                params['days_of_week'] = self.days_of_week.to_alipay_dict()
            else:
                params['days_of_week'] = self.days_of_week
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.end_time_type:
            if hasattr(self.end_time_type, 'to_alipay_dict'):
                params['end_time_type'] = self.end_time_type.to_alipay_dict()
            else:
                params['end_time_type'] = self.end_time_type
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
        o = LimitDayInfo()
        if 'days_of_week' in d:
            o.days_of_week = d['days_of_week']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'end_time_type' in d:
            o.end_time_type = d['end_time_type']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


