#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CanNoUseLimitDayInfo(object):

    def __init__(self):
        self._end_date = None
        self._end_time = None
        self._end_time_type = None
        self._start_date = None
        self._start_time = None

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
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
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
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
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
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
        o = CanNoUseLimitDayInfo()
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'end_time_type' in d:
            o.end_time_type = d['end_time_type']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


