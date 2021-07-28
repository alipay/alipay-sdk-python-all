#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PrizeValidPeriod(object):

    def __init__(self):
        self._active_min = None
        self._active_mins = None
        self._active_time = None
        self._end_min = None
        self._end_mins = None
        self._end_time = None
        self._period_type = None

    @property
    def active_min(self):
        return self._active_min

    @active_min.setter
    def active_min(self, value):
        self._active_min = value
    @property
    def active_mins(self):
        return self._active_mins

    @active_mins.setter
    def active_mins(self, value):
        self._active_mins = value
    @property
    def active_time(self):
        return self._active_time

    @active_time.setter
    def active_time(self, value):
        self._active_time = value
    @property
    def end_min(self):
        return self._end_min

    @end_min.setter
    def end_min(self, value):
        self._end_min = value
    @property
    def end_mins(self):
        return self._end_mins

    @end_mins.setter
    def end_mins(self, value):
        self._end_mins = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def period_type(self):
        return self._period_type

    @period_type.setter
    def period_type(self, value):
        self._period_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.active_min:
            if hasattr(self.active_min, 'to_alipay_dict'):
                params['active_min'] = self.active_min.to_alipay_dict()
            else:
                params['active_min'] = self.active_min
        if self.active_mins:
            if hasattr(self.active_mins, 'to_alipay_dict'):
                params['active_mins'] = self.active_mins.to_alipay_dict()
            else:
                params['active_mins'] = self.active_mins
        if self.active_time:
            if hasattr(self.active_time, 'to_alipay_dict'):
                params['active_time'] = self.active_time.to_alipay_dict()
            else:
                params['active_time'] = self.active_time
        if self.end_min:
            if hasattr(self.end_min, 'to_alipay_dict'):
                params['end_min'] = self.end_min.to_alipay_dict()
            else:
                params['end_min'] = self.end_min
        if self.end_mins:
            if hasattr(self.end_mins, 'to_alipay_dict'):
                params['end_mins'] = self.end_mins.to_alipay_dict()
            else:
                params['end_mins'] = self.end_mins
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.period_type:
            if hasattr(self.period_type, 'to_alipay_dict'):
                params['period_type'] = self.period_type.to_alipay_dict()
            else:
                params['period_type'] = self.period_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PrizeValidPeriod()
        if 'active_min' in d:
            o.active_min = d['active_min']
        if 'active_mins' in d:
            o.active_mins = d['active_mins']
        if 'active_time' in d:
            o.active_time = d['active_time']
        if 'end_min' in d:
            o.end_min = d['end_min']
        if 'end_mins' in d:
            o.end_mins = d['end_mins']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'period_type' in d:
            o.period_type = d['period_type']
        return o


