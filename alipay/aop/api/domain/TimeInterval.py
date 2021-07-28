#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TimeInterval(object):

    def __init__(self):
        self._end_time = None
        self._ext_param = None
        self._max_time_interval = None
        self._min_time_interval = None
        self._start_time = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
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
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
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
        o = TimeInterval()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'max_time_interval' in d:
            o.max_time_interval = d['max_time_interval']
        if 'min_time_interval' in d:
            o.min_time_interval = d['min_time_interval']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


