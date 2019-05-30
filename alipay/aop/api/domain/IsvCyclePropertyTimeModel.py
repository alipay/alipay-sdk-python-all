#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IsvCyclePropertyTimeModel(object):

    def __init__(self):
        self._date = None
        self._time_type = None
        self._week = None

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def time_type(self):
        return self._time_type

    @time_type.setter
    def time_type(self, value):
        self._time_type = value
    @property
    def week(self):
        return self._week

    @week.setter
    def week(self, value):
        self._week = value


    def to_alipay_dict(self):
        params = dict()
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.time_type:
            if hasattr(self.time_type, 'to_alipay_dict'):
                params['time_type'] = self.time_type.to_alipay_dict()
            else:
                params['time_type'] = self.time_type
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
        o = IsvCyclePropertyTimeModel()
        if 'date' in d:
            o.date = d['date']
        if 'time_type' in d:
            o.time_type = d['time_type']
        if 'week' in d:
            o.week = d['week']
        return o


