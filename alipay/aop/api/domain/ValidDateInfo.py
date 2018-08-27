#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PeriodInfo import PeriodInfo


class ValidDateInfo(object):

    def __init__(self):
        self._end_time = None
        self._relative_time = None
        self._start_time = None
        self._time_mode = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def relative_time(self):
        return self._relative_time

    @relative_time.setter
    def relative_time(self, value):
        if isinstance(value, PeriodInfo):
            self._relative_time = value
        else:
            self._relative_time = PeriodInfo.from_alipay_dict(value)
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def time_mode(self):
        return self._time_mode

    @time_mode.setter
    def time_mode(self, value):
        self._time_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.relative_time:
            if hasattr(self.relative_time, 'to_alipay_dict'):
                params['relative_time'] = self.relative_time.to_alipay_dict()
            else:
                params['relative_time'] = self.relative_time
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.time_mode:
            if hasattr(self.time_mode, 'to_alipay_dict'):
                params['time_mode'] = self.time_mode.to_alipay_dict()
            else:
                params['time_mode'] = self.time_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ValidDateInfo()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'relative_time' in d:
            o.relative_time = d['relative_time']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'time_mode' in d:
            o.time_mode = d['time_mode']
        return o


