#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherTimeRule(object):

    def __init__(self):
        self._days = None
        self._end_time = None
        self._start_time = None
        self._time_type = None

    @property
    def days(self):
        return self._days

    @days.setter
    def days(self, value):
        self._days = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def time_type(self):
        return self._time_type

    @time_type.setter
    def time_type(self, value):
        self._time_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.days:
            if hasattr(self.days, 'to_alipay_dict'):
                params['days'] = self.days.to_alipay_dict()
            else:
                params['days'] = self.days
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.time_type:
            if hasattr(self.time_type, 'to_alipay_dict'):
                params['time_type'] = self.time_type.to_alipay_dict()
            else:
                params['time_type'] = self.time_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherTimeRule()
        if 'days' in d:
            o.days = d['days']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'time_type' in d:
            o.time_type = d['time_type']
        return o


