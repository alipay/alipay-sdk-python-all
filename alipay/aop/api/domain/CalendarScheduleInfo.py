#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ScheduleInfo import ScheduleInfo


class CalendarScheduleInfo(object):

    def __init__(self):
        self._duration = None
        self._schedule = None
        self._unit = None

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
    @property
    def schedule(self):
        return self._schedule

    @schedule.setter
    def schedule(self, value):
        if isinstance(value, list):
            self._schedule = list()
            for i in value:
                if isinstance(i, ScheduleInfo):
                    self._schedule.append(i)
                else:
                    self._schedule.append(ScheduleInfo.from_alipay_dict(i))
    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.duration:
            if hasattr(self.duration, 'to_alipay_dict'):
                params['duration'] = self.duration.to_alipay_dict()
            else:
                params['duration'] = self.duration
        if self.schedule:
            if isinstance(self.schedule, list):
                for i in range(0, len(self.schedule)):
                    element = self.schedule[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.schedule[i] = element.to_alipay_dict()
            if hasattr(self.schedule, 'to_alipay_dict'):
                params['schedule'] = self.schedule.to_alipay_dict()
            else:
                params['schedule'] = self.schedule
        if self.unit:
            if hasattr(self.unit, 'to_alipay_dict'):
                params['unit'] = self.unit.to_alipay_dict()
            else:
                params['unit'] = self.unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CalendarScheduleInfo()
        if 'duration' in d:
            o.duration = d['duration']
        if 'schedule' in d:
            o.schedule = d['schedule']
        if 'unit' in d:
            o.unit = d['unit']
        return o


