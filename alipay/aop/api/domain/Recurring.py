#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Recurring(object):

    def __init__(self):
        self._interval = None
        self._interval_count = None
        self._trial_period_days = None
        self._usage_type = None

    @property
    def interval(self):
        return self._interval

    @interval.setter
    def interval(self, value):
        self._interval = value
    @property
    def interval_count(self):
        return self._interval_count

    @interval_count.setter
    def interval_count(self, value):
        self._interval_count = value
    @property
    def trial_period_days(self):
        return self._trial_period_days

    @trial_period_days.setter
    def trial_period_days(self, value):
        self._trial_period_days = value
    @property
    def usage_type(self):
        return self._usage_type

    @usage_type.setter
    def usage_type(self, value):
        self._usage_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.interval:
            if hasattr(self.interval, 'to_alipay_dict'):
                params['interval'] = self.interval.to_alipay_dict()
            else:
                params['interval'] = self.interval
        if self.interval_count:
            if hasattr(self.interval_count, 'to_alipay_dict'):
                params['interval_count'] = self.interval_count.to_alipay_dict()
            else:
                params['interval_count'] = self.interval_count
        if self.trial_period_days:
            if hasattr(self.trial_period_days, 'to_alipay_dict'):
                params['trial_period_days'] = self.trial_period_days.to_alipay_dict()
            else:
                params['trial_period_days'] = self.trial_period_days
        if self.usage_type:
            if hasattr(self.usage_type, 'to_alipay_dict'):
                params['usage_type'] = self.usage_type.to_alipay_dict()
            else:
                params['usage_type'] = self.usage_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Recurring()
        if 'interval' in d:
            o.interval = d['interval']
        if 'interval_count' in d:
            o.interval_count = d['interval_count']
        if 'trial_period_days' in d:
            o.trial_period_days = d['trial_period_days']
        if 'usage_type' in d:
            o.usage_type = d['usage_type']
        return o


