#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DtBankActivityTimeInfo(object):

    def __init__(self):
        self._begin_time = None
        self._end_time = None
        self._time_period_list = None
        self._week_day_list = None

    @property
    def begin_time(self):
        return self._begin_time

    @begin_time.setter
    def begin_time(self, value):
        self._begin_time = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def time_period_list(self):
        return self._time_period_list

    @time_period_list.setter
    def time_period_list(self, value):
        if isinstance(value, list):
            self._time_period_list = list()
            for i in value:
                self._time_period_list.append(i)
    @property
    def week_day_list(self):
        return self._week_day_list

    @week_day_list.setter
    def week_day_list(self, value):
        if isinstance(value, list):
            self._week_day_list = list()
            for i in value:
                self._week_day_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.begin_time:
            if hasattr(self.begin_time, 'to_alipay_dict'):
                params['begin_time'] = self.begin_time.to_alipay_dict()
            else:
                params['begin_time'] = self.begin_time
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
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
        if self.week_day_list:
            if isinstance(self.week_day_list, list):
                for i in range(0, len(self.week_day_list)):
                    element = self.week_day_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.week_day_list[i] = element.to_alipay_dict()
            if hasattr(self.week_day_list, 'to_alipay_dict'):
                params['week_day_list'] = self.week_day_list.to_alipay_dict()
            else:
                params['week_day_list'] = self.week_day_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DtBankActivityTimeInfo()
        if 'begin_time' in d:
            o.begin_time = d['begin_time']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'time_period_list' in d:
            o.time_period_list = d['time_period_list']
        if 'week_day_list' in d:
            o.week_day_list = d['week_day_list']
        return o


