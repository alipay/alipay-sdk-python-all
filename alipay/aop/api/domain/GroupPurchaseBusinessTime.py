#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GroupPurchaseTimePeriod import GroupPurchaseTimePeriod


class GroupPurchaseBusinessTime(object):

    def __init__(self):
        self._days = None
        self._open_24_hours = None
        self._times = None

    @property
    def days(self):
        return self._days

    @days.setter
    def days(self, value):
        if isinstance(value, list):
            self._days = list()
            for i in value:
                self._days.append(i)
    @property
    def open_24_hours(self):
        return self._open_24_hours

    @open_24_hours.setter
    def open_24_hours(self, value):
        self._open_24_hours = value
    @property
    def times(self):
        return self._times

    @times.setter
    def times(self, value):
        if isinstance(value, list):
            self._times = list()
            for i in value:
                if isinstance(i, GroupPurchaseTimePeriod):
                    self._times.append(i)
                else:
                    self._times.append(GroupPurchaseTimePeriod.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.days:
            if isinstance(self.days, list):
                for i in range(0, len(self.days)):
                    element = self.days[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.days[i] = element.to_alipay_dict()
            if hasattr(self.days, 'to_alipay_dict'):
                params['days'] = self.days.to_alipay_dict()
            else:
                params['days'] = self.days
        if self.open_24_hours:
            if hasattr(self.open_24_hours, 'to_alipay_dict'):
                params['open_24_hours'] = self.open_24_hours.to_alipay_dict()
            else:
                params['open_24_hours'] = self.open_24_hours
        if self.times:
            if isinstance(self.times, list):
                for i in range(0, len(self.times)):
                    element = self.times[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.times[i] = element.to_alipay_dict()
            if hasattr(self.times, 'to_alipay_dict'):
                params['times'] = self.times.to_alipay_dict()
            else:
                params['times'] = self.times
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupPurchaseBusinessTime()
        if 'days' in d:
            o.days = d['days']
        if 'open_24_hours' in d:
            o.open_24_hours = d['open_24_hours']
        if 'times' in d:
            o.times = d['times']
        return o


