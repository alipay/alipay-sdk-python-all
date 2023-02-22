#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TimeRangeInfo import TimeRangeInfo


class WeekRuleInfo(object):

    def __init__(self):
        self._time_range_info = None
        self._week_day = None

    @property
    def time_range_info(self):
        return self._time_range_info

    @time_range_info.setter
    def time_range_info(self, value):
        if isinstance(value, TimeRangeInfo):
            self._time_range_info = value
        else:
            self._time_range_info = TimeRangeInfo.from_alipay_dict(value)
    @property
    def week_day(self):
        return self._week_day

    @week_day.setter
    def week_day(self, value):
        self._week_day = value


    def to_alipay_dict(self):
        params = dict()
        if self.time_range_info:
            if hasattr(self.time_range_info, 'to_alipay_dict'):
                params['time_range_info'] = self.time_range_info.to_alipay_dict()
            else:
                params['time_range_info'] = self.time_range_info
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
        o = WeekRuleInfo()
        if 'time_range_info' in d:
            o.time_range_info = d['time_range_info']
        if 'week_day' in d:
            o.week_day = d['week_day']
        return o


