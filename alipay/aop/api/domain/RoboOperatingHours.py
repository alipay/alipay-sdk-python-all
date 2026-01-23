#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RoboTimeSlot import RoboTimeSlot


class RoboOperatingHours(object):

    def __init__(self):
        self._day = None
        self._time = None

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        if isinstance(value, list):
            self._day = list()
            for i in value:
                self._day.append(i)
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        if isinstance(value, list):
            self._time = list()
            for i in value:
                if isinstance(i, RoboTimeSlot):
                    self._time.append(i)
                else:
                    self._time.append(RoboTimeSlot.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.day:
            if isinstance(self.day, list):
                for i in range(0, len(self.day)):
                    element = self.day[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.day[i] = element.to_alipay_dict()
            if hasattr(self.day, 'to_alipay_dict'):
                params['day'] = self.day.to_alipay_dict()
            else:
                params['day'] = self.day
        if self.time:
            if isinstance(self.time, list):
                for i in range(0, len(self.time)):
                    element = self.time[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.time[i] = element.to_alipay_dict()
            if hasattr(self.time, 'to_alipay_dict'):
                params['time'] = self.time.to_alipay_dict()
            else:
                params['time'] = self.time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RoboOperatingHours()
        if 'day' in d:
            o.day = d['day']
        if 'time' in d:
            o.time = d['time']
        return o


