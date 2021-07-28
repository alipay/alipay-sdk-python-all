#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ScheduleWorkStatItem import ScheduleWorkStatItem
from alipay.aop.api.domain.ScheduleWorkItem import ScheduleWorkItem


class ScheduleWorkItems(object):

    def __init__(self):
        self._stats = None
        self._work = None

    @property
    def stats(self):
        return self._stats

    @stats.setter
    def stats(self, value):
        if isinstance(value, list):
            self._stats = list()
            for i in value:
                if isinstance(i, ScheduleWorkStatItem):
                    self._stats.append(i)
                else:
                    self._stats.append(ScheduleWorkStatItem.from_alipay_dict(i))
    @property
    def work(self):
        return self._work

    @work.setter
    def work(self, value):
        if isinstance(value, list):
            self._work = list()
            for i in value:
                if isinstance(i, ScheduleWorkItem):
                    self._work.append(i)
                else:
                    self._work.append(ScheduleWorkItem.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.stats:
            if isinstance(self.stats, list):
                for i in range(0, len(self.stats)):
                    element = self.stats[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.stats[i] = element.to_alipay_dict()
            if hasattr(self.stats, 'to_alipay_dict'):
                params['stats'] = self.stats.to_alipay_dict()
            else:
                params['stats'] = self.stats
        if self.work:
            if isinstance(self.work, list):
                for i in range(0, len(self.work)):
                    element = self.work[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.work[i] = element.to_alipay_dict()
            if hasattr(self.work, 'to_alipay_dict'):
                params['work'] = self.work.to_alipay_dict()
            else:
                params['work'] = self.work
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ScheduleWorkItems()
        if 'stats' in d:
            o.stats = d['stats']
        if 'work' in d:
            o.work = d['work']
        return o


