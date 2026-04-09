#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecurringConfig(object):

    def __init__(self):
        self._interval = None
        self._interval_count = None

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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecurringConfig()
        if 'interval' in d:
            o.interval = d['interval']
        if 'interval_count' in d:
            o.interval_count = d['interval_count']
        return o


