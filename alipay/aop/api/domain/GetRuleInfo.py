#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PeriodInfo import PeriodInfo


class GetRuleInfo(object):

    def __init__(self):
        self._end_time = None
        self._get_count_limit = None
        self._start_time = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def get_count_limit(self):
        return self._get_count_limit

    @get_count_limit.setter
    def get_count_limit(self, value):
        if isinstance(value, PeriodInfo):
            self._get_count_limit = value
        else:
            self._get_count_limit = PeriodInfo.from_alipay_dict(value)
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.get_count_limit:
            if hasattr(self.get_count_limit, 'to_alipay_dict'):
                params['get_count_limit'] = self.get_count_limit.to_alipay_dict()
            else:
                params['get_count_limit'] = self.get_count_limit
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GetRuleInfo()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'get_count_limit' in d:
            o.get_count_limit = d['get_count_limit']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


