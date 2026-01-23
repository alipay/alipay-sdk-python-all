#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivityTimeRange import ActivityTimeRange


class ActivityPromotionDuration(object):

    def __init__(self):
        self._allowed_days = None
        self._allowed_times = None
        self._limit_type = None

    @property
    def allowed_days(self):
        return self._allowed_days

    @allowed_days.setter
    def allowed_days(self, value):
        if isinstance(value, list):
            self._allowed_days = list()
            for i in value:
                self._allowed_days.append(i)
    @property
    def allowed_times(self):
        return self._allowed_times

    @allowed_times.setter
    def allowed_times(self, value):
        if isinstance(value, list):
            self._allowed_times = list()
            for i in value:
                if isinstance(i, ActivityTimeRange):
                    self._allowed_times.append(i)
                else:
                    self._allowed_times.append(ActivityTimeRange.from_alipay_dict(i))
    @property
    def limit_type(self):
        return self._limit_type

    @limit_type.setter
    def limit_type(self, value):
        self._limit_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.allowed_days:
            if isinstance(self.allowed_days, list):
                for i in range(0, len(self.allowed_days)):
                    element = self.allowed_days[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.allowed_days[i] = element.to_alipay_dict()
            if hasattr(self.allowed_days, 'to_alipay_dict'):
                params['allowed_days'] = self.allowed_days.to_alipay_dict()
            else:
                params['allowed_days'] = self.allowed_days
        if self.allowed_times:
            if isinstance(self.allowed_times, list):
                for i in range(0, len(self.allowed_times)):
                    element = self.allowed_times[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.allowed_times[i] = element.to_alipay_dict()
            if hasattr(self.allowed_times, 'to_alipay_dict'):
                params['allowed_times'] = self.allowed_times.to_alipay_dict()
            else:
                params['allowed_times'] = self.allowed_times
        if self.limit_type:
            if hasattr(self.limit_type, 'to_alipay_dict'):
                params['limit_type'] = self.limit_type.to_alipay_dict()
            else:
                params['limit_type'] = self.limit_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivityPromotionDuration()
        if 'allowed_days' in d:
            o.allowed_days = d['allowed_days']
        if 'allowed_times' in d:
            o.allowed_times = d['allowed_times']
        if 'limit_type' in d:
            o.limit_type = d['limit_type']
        return o


