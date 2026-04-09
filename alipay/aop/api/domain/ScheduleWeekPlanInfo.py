#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ScheduleWeekPlanInfo(object):

    def __init__(self):
        self._break_time = None
        self._close_time = None
        self._day_of_week = None
        self._open_time = None

    @property
    def break_time(self):
        return self._break_time

    @break_time.setter
    def break_time(self, value):
        if isinstance(value, list):
            self._break_time = list()
            for i in value:
                self._break_time.append(i)
    @property
    def close_time(self):
        return self._close_time

    @close_time.setter
    def close_time(self, value):
        self._close_time = value
    @property
    def day_of_week(self):
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, value):
        self._day_of_week = value
    @property
    def open_time(self):
        return self._open_time

    @open_time.setter
    def open_time(self, value):
        self._open_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.break_time:
            if isinstance(self.break_time, list):
                for i in range(0, len(self.break_time)):
                    element = self.break_time[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.break_time[i] = element.to_alipay_dict()
            if hasattr(self.break_time, 'to_alipay_dict'):
                params['break_time'] = self.break_time.to_alipay_dict()
            else:
                params['break_time'] = self.break_time
        if self.close_time:
            if hasattr(self.close_time, 'to_alipay_dict'):
                params['close_time'] = self.close_time.to_alipay_dict()
            else:
                params['close_time'] = self.close_time
        if self.day_of_week:
            if hasattr(self.day_of_week, 'to_alipay_dict'):
                params['day_of_week'] = self.day_of_week.to_alipay_dict()
            else:
                params['day_of_week'] = self.day_of_week
        if self.open_time:
            if hasattr(self.open_time, 'to_alipay_dict'):
                params['open_time'] = self.open_time.to_alipay_dict()
            else:
                params['open_time'] = self.open_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ScheduleWeekPlanInfo()
        if 'break_time' in d:
            o.break_time = d['break_time']
        if 'close_time' in d:
            o.close_time = d['close_time']
        if 'day_of_week' in d:
            o.day_of_week = d['day_of_week']
        if 'open_time' in d:
            o.open_time = d['open_time']
        return o


