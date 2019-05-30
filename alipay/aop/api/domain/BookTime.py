#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BookTime(object):

    def __init__(self):
        self._time = None
        self._week = None

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        if isinstance(value, list):
            self._time = list()
            for i in value:
                self._time.append(i)
    @property
    def week(self):
        return self._week

    @week.setter
    def week(self, value):
        self._week = value


    def to_alipay_dict(self):
        params = dict()
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
        o = BookTime()
        if 'time' in d:
            o.time = d['time']
        if 'week' in d:
            o.week = d['week']
        return o


