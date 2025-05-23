#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ComplexBusinessTimePeriod import ComplexBusinessTimePeriod


class ComplexBusinessTime(object):

    def __init__(self):
        self._time_period = None
        self._week_day = None

    @property
    def time_period(self):
        return self._time_period

    @time_period.setter
    def time_period(self, value):
        if isinstance(value, list):
            self._time_period = list()
            for i in value:
                if isinstance(i, ComplexBusinessTimePeriod):
                    self._time_period.append(i)
                else:
                    self._time_period.append(ComplexBusinessTimePeriod.from_alipay_dict(i))
    @property
    def week_day(self):
        return self._week_day

    @week_day.setter
    def week_day(self, value):
        self._week_day = value


    def to_alipay_dict(self):
        params = dict()
        if self.time_period:
            if isinstance(self.time_period, list):
                for i in range(0, len(self.time_period)):
                    element = self.time_period[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.time_period[i] = element.to_alipay_dict()
            if hasattr(self.time_period, 'to_alipay_dict'):
                params['time_period'] = self.time_period.to_alipay_dict()
            else:
                params['time_period'] = self.time_period
        if self.week_day:
            if hasattr(self.week_day, 'to_alipay_dict'):
                params['week_day'] = self.week_day.to_alipay_dict()
            else:
                params['week_day'] = self.week_day
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ComplexBusinessTime()
        if 'time_period' in d:
            o.time_period = d['time_period']
        if 'week_day' in d:
            o.week_day = d['week_day']
        return o


