#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BusinessDateDTO(object):

    def __init__(self):
        self._week_day = None
        self._work_time = None

    @property
    def week_day(self):
        return self._week_day

    @week_day.setter
    def week_day(self, value):
        if isinstance(value, list):
            self._week_day = list()
            for i in value:
                self._week_day.append(i)
    @property
    def work_time(self):
        return self._work_time

    @work_time.setter
    def work_time(self, value):
        if isinstance(value, list):
            self._work_time = list()
            for i in value:
                self._work_time.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.week_day:
            if isinstance(self.week_day, list):
                for i in range(0, len(self.week_day)):
                    element = self.week_day[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.week_day[i] = element.to_alipay_dict()
            if hasattr(self.week_day, 'to_alipay_dict'):
                params['week_day'] = self.week_day.to_alipay_dict()
            else:
                params['week_day'] = self.week_day
        if self.work_time:
            if isinstance(self.work_time, list):
                for i in range(0, len(self.work_time)):
                    element = self.work_time[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.work_time[i] = element.to_alipay_dict()
            if hasattr(self.work_time, 'to_alipay_dict'):
                params['work_time'] = self.work_time.to_alipay_dict()
            else:
                params['work_time'] = self.work_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BusinessDateDTO()
        if 'week_day' in d:
            o.week_day = d['week_day']
        if 'work_time' in d:
            o.work_time = d['work_time']
        return o


