#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ScheduleOdItem(object):

    def __init__(self):
        self._cluster_class = None
        self._direction = None
        self._end_load = None
        self._end_load_percent = None
        self._end_name = None
        self._end_num = None
        self._line_id = None
        self._start_load = None
        self._start_name = None
        self._start_num = None
        self._time_period = None

    @property
    def cluster_class(self):
        return self._cluster_class

    @cluster_class.setter
    def cluster_class(self, value):
        self._cluster_class = value
    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value
    @property
    def end_load(self):
        return self._end_load

    @end_load.setter
    def end_load(self, value):
        self._end_load = value
    @property
    def end_load_percent(self):
        return self._end_load_percent

    @end_load_percent.setter
    def end_load_percent(self, value):
        self._end_load_percent = value
    @property
    def end_name(self):
        return self._end_name

    @end_name.setter
    def end_name(self, value):
        self._end_name = value
    @property
    def end_num(self):
        return self._end_num

    @end_num.setter
    def end_num(self, value):
        self._end_num = value
    @property
    def line_id(self):
        return self._line_id

    @line_id.setter
    def line_id(self, value):
        self._line_id = value
    @property
    def start_load(self):
        return self._start_load

    @start_load.setter
    def start_load(self, value):
        self._start_load = value
    @property
    def start_name(self):
        return self._start_name

    @start_name.setter
    def start_name(self, value):
        self._start_name = value
    @property
    def start_num(self):
        return self._start_num

    @start_num.setter
    def start_num(self, value):
        self._start_num = value
    @property
    def time_period(self):
        return self._time_period

    @time_period.setter
    def time_period(self, value):
        self._time_period = value


    def to_alipay_dict(self):
        params = dict()
        if self.cluster_class:
            if hasattr(self.cluster_class, 'to_alipay_dict'):
                params['cluster_class'] = self.cluster_class.to_alipay_dict()
            else:
                params['cluster_class'] = self.cluster_class
        if self.direction:
            if hasattr(self.direction, 'to_alipay_dict'):
                params['direction'] = self.direction.to_alipay_dict()
            else:
                params['direction'] = self.direction
        if self.end_load:
            if hasattr(self.end_load, 'to_alipay_dict'):
                params['end_load'] = self.end_load.to_alipay_dict()
            else:
                params['end_load'] = self.end_load
        if self.end_load_percent:
            if hasattr(self.end_load_percent, 'to_alipay_dict'):
                params['end_load_percent'] = self.end_load_percent.to_alipay_dict()
            else:
                params['end_load_percent'] = self.end_load_percent
        if self.end_name:
            if hasattr(self.end_name, 'to_alipay_dict'):
                params['end_name'] = self.end_name.to_alipay_dict()
            else:
                params['end_name'] = self.end_name
        if self.end_num:
            if hasattr(self.end_num, 'to_alipay_dict'):
                params['end_num'] = self.end_num.to_alipay_dict()
            else:
                params['end_num'] = self.end_num
        if self.line_id:
            if hasattr(self.line_id, 'to_alipay_dict'):
                params['line_id'] = self.line_id.to_alipay_dict()
            else:
                params['line_id'] = self.line_id
        if self.start_load:
            if hasattr(self.start_load, 'to_alipay_dict'):
                params['start_load'] = self.start_load.to_alipay_dict()
            else:
                params['start_load'] = self.start_load
        if self.start_name:
            if hasattr(self.start_name, 'to_alipay_dict'):
                params['start_name'] = self.start_name.to_alipay_dict()
            else:
                params['start_name'] = self.start_name
        if self.start_num:
            if hasattr(self.start_num, 'to_alipay_dict'):
                params['start_num'] = self.start_num.to_alipay_dict()
            else:
                params['start_num'] = self.start_num
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
        o = ScheduleOdItem()
        if 'cluster_class' in d:
            o.cluster_class = d['cluster_class']
        if 'direction' in d:
            o.direction = d['direction']
        if 'end_load' in d:
            o.end_load = d['end_load']
        if 'end_load_percent' in d:
            o.end_load_percent = d['end_load_percent']
        if 'end_name' in d:
            o.end_name = d['end_name']
        if 'end_num' in d:
            o.end_num = d['end_num']
        if 'line_id' in d:
            o.line_id = d['line_id']
        if 'start_load' in d:
            o.start_load = d['start_load']
        if 'start_name' in d:
            o.start_name = d['start_name']
        if 'start_num' in d:
            o.start_num = d['start_num']
        if 'time_period' in d:
            o.time_period = d['time_period']
        return o


