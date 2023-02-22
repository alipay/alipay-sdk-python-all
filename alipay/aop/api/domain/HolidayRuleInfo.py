#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TimeRangeInfo import TimeRangeInfo


class HolidayRuleInfo(object):

    def __init__(self):
        self._time_range_info = None

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
        o = HolidayRuleInfo()
        if 'time_range_info' in d:
            o.time_range_info = d['time_range_info']
        return o


