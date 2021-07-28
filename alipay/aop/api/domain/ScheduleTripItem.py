#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ScheduleTripItem(object):

    def __init__(self):
        self._direction = None
        self._line_id = None
        self._run_time = None
        self._time_period = None

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value
    @property
    def line_id(self):
        return self._line_id

    @line_id.setter
    def line_id(self, value):
        self._line_id = value
    @property
    def run_time(self):
        return self._run_time

    @run_time.setter
    def run_time(self, value):
        self._run_time = value
    @property
    def time_period(self):
        return self._time_period

    @time_period.setter
    def time_period(self, value):
        self._time_period = value


    def to_alipay_dict(self):
        params = dict()
        if self.direction:
            if hasattr(self.direction, 'to_alipay_dict'):
                params['direction'] = self.direction.to_alipay_dict()
            else:
                params['direction'] = self.direction
        if self.line_id:
            if hasattr(self.line_id, 'to_alipay_dict'):
                params['line_id'] = self.line_id.to_alipay_dict()
            else:
                params['line_id'] = self.line_id
        if self.run_time:
            if hasattr(self.run_time, 'to_alipay_dict'):
                params['run_time'] = self.run_time.to_alipay_dict()
            else:
                params['run_time'] = self.run_time
        if self.time_period:
            if hasattr(self.time_period, 'to_alipay_dict'):
                params['time_period'] = self.time_period.to_alipay_dict()
            else:
                params['time_period'] = self.time_period
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ScheduleTripItem()
        if 'direction' in d:
            o.direction = d['direction']
        if 'line_id' in d:
            o.line_id = d['line_id']
        if 'run_time' in d:
            o.run_time = d['run_time']
        if 'time_period' in d:
            o.time_period = d['time_period']
        return o


