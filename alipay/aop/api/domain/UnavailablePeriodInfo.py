#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UnavailablePeriodInfo(object):

    def __init__(self):
        self._end_day = None
        self._start_day = None

    @property
    def end_day(self):
        return self._end_day

    @end_day.setter
    def end_day(self, value):
        self._end_day = value
    @property
    def start_day(self):
        return self._start_day

    @start_day.setter
    def start_day(self, value):
        self._start_day = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_day:
            if hasattr(self.end_day, 'to_alipay_dict'):
                params['end_day'] = self.end_day.to_alipay_dict()
            else:
                params['end_day'] = self.end_day
        if self.start_day:
            if hasattr(self.start_day, 'to_alipay_dict'):
                params['start_day'] = self.start_day.to_alipay_dict()
            else:
                params['start_day'] = self.start_day
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UnavailablePeriodInfo()
        if 'end_day' in d:
            o.end_day = d['end_day']
        if 'start_day' in d:
            o.start_day = d['start_day']
        return o


