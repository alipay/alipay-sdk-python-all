#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TimeRange import TimeRange


class NormalBusinessTimeRule(object):

    def __init__(self):
        self._month = None
        self._open_time_list = None
        self._week = None

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        if isinstance(value, list):
            self._month = list()
            for i in value:
                self._month.append(i)
    @property
    def open_time_list(self):
        return self._open_time_list

    @open_time_list.setter
    def open_time_list(self, value):
        if isinstance(value, list):
            self._open_time_list = list()
            for i in value:
                if isinstance(i, TimeRange):
                    self._open_time_list.append(i)
                else:
                    self._open_time_list.append(TimeRange.from_alipay_dict(i))
    @property
    def week(self):
        return self._week

    @week.setter
    def week(self, value):
        if isinstance(value, list):
            self._week = list()
            for i in value:
                self._week.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.month:
            if isinstance(self.month, list):
                for i in range(0, len(self.month)):
                    element = self.month[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.month[i] = element.to_alipay_dict()
            if hasattr(self.month, 'to_alipay_dict'):
                params['month'] = self.month.to_alipay_dict()
            else:
                params['month'] = self.month
        if self.open_time_list:
            if isinstance(self.open_time_list, list):
                for i in range(0, len(self.open_time_list)):
                    element = self.open_time_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.open_time_list[i] = element.to_alipay_dict()
            if hasattr(self.open_time_list, 'to_alipay_dict'):
                params['open_time_list'] = self.open_time_list.to_alipay_dict()
            else:
                params['open_time_list'] = self.open_time_list
        if self.week:
            if isinstance(self.week, list):
                for i in range(0, len(self.week)):
                    element = self.week[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.week[i] = element.to_alipay_dict()
            if hasattr(self.week, 'to_alipay_dict'):
                params['week'] = self.week.to_alipay_dict()
            else:
                params['week'] = self.week
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NormalBusinessTimeRule()
        if 'month' in d:
            o.month = d['month']
        if 'open_time_list' in d:
            o.open_time_list = d['open_time_list']
        if 'week' in d:
            o.week = d['week']
        return o


