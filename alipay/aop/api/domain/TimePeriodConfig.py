#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TimePeriod import TimePeriod


class TimePeriodConfig(object):

    def __init__(self):
        self._time_period_list = None
        self._week = None

    @property
    def time_period_list(self):
        return self._time_period_list

    @time_period_list.setter
    def time_period_list(self, value):
        if isinstance(value, list):
            self._time_period_list = list()
            for i in value:
                if isinstance(i, TimePeriod):
                    self._time_period_list.append(i)
                else:
                    self._time_period_list.append(TimePeriod.from_alipay_dict(i))
    @property
    def week(self):
        return self._week

    @week.setter
    def week(self, value):
        self._week = value


    def to_alipay_dict(self):
        params = dict()
        if self.time_period_list:
            if isinstance(self.time_period_list, list):
                for i in range(0, len(self.time_period_list)):
                    element = self.time_period_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.time_period_list[i] = element.to_alipay_dict()
            if hasattr(self.time_period_list, 'to_alipay_dict'):
                params['time_period_list'] = self.time_period_list.to_alipay_dict()
            else:
                params['time_period_list'] = self.time_period_list
        if self.week:
            if hasattr(self.week, 'to_alipay_dict'):
                params['week'] = self.week.to_alipay_dict()
            else:
                params['week'] = self.week
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TimePeriodConfig()
        if 'time_period_list' in d:
            o.time_period_list = d['time_period_list']
        if 'week' in d:
            o.week = d['week']
        return o


