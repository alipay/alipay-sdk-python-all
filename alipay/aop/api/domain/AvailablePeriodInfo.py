#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AvailablePeriodInfo(object):

    def __init__(self):
        self._available_week_days = None
        self._time_end = None
        self._time_start = None

    @property
    def available_week_days(self):
        return self._available_week_days

    @available_week_days.setter
    def available_week_days(self, value):
        self._available_week_days = value
    @property
    def time_end(self):
        return self._time_end

    @time_end.setter
    def time_end(self, value):
        self._time_end = value
    @property
    def time_start(self):
        return self._time_start

    @time_start.setter
    def time_start(self, value):
        self._time_start = value


    def to_alipay_dict(self):
        params = dict()
        if self.available_week_days:
            if hasattr(self.available_week_days, 'to_alipay_dict'):
                params['available_week_days'] = self.available_week_days.to_alipay_dict()
            else:
                params['available_week_days'] = self.available_week_days
        if self.time_end:
            if hasattr(self.time_end, 'to_alipay_dict'):
                params['time_end'] = self.time_end.to_alipay_dict()
            else:
                params['time_end'] = self.time_end
        if self.time_start:
            if hasattr(self.time_start, 'to_alipay_dict'):
                params['time_start'] = self.time_start.to_alipay_dict()
            else:
                params['time_start'] = self.time_start
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AvailablePeriodInfo()
        if 'available_week_days' in d:
            o.available_week_days = d['available_week_days']
        if 'time_end' in d:
            o.time_end = d['time_end']
        if 'time_start' in d:
            o.time_start = d['time_start']
        return o


