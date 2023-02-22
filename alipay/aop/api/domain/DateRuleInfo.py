#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DateRangeInfo import DateRangeInfo
from alipay.aop.api.domain.TimeRangeInfo import TimeRangeInfo


class DateRuleInfo(object):

    def __init__(self):
        self._date_range_info = None
        self._time_range_info = None

    @property
    def date_range_info(self):
        return self._date_range_info

    @date_range_info.setter
    def date_range_info(self, value):
        if isinstance(value, DateRangeInfo):
            self._date_range_info = value
        else:
            self._date_range_info = DateRangeInfo.from_alipay_dict(value)
    @property
    def time_range_info(self):
        return self._time_range_info

    @time_range_info.setter
    def time_range_info(self, value):
        if isinstance(value, TimeRangeInfo):
            self._time_range_info = value
        else:
            self._time_range_info = TimeRangeInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.date_range_info:
            if hasattr(self.date_range_info, 'to_alipay_dict'):
                params['date_range_info'] = self.date_range_info.to_alipay_dict()
            else:
                params['date_range_info'] = self.date_range_info
        if self.time_range_info:
            if hasattr(self.time_range_info, 'to_alipay_dict'):
                params['time_range_info'] = self.time_range_info.to_alipay_dict()
            else:
                params['time_range_info'] = self.time_range_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DateRuleInfo()
        if 'date_range_info' in d:
            o.date_range_info = d['date_range_info']
        if 'time_range_info' in d:
            o.time_range_info = d['time_range_info']
        return o


