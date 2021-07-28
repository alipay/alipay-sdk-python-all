#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbdishTimeRangeInfo import KbdishTimeRangeInfo


class KbdishPeriodExtendInfo(object):

    def __init__(self):
        self._end_date = None
        self._start_date = None
        self._time_range_list = None
        self._weeks = None

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def time_range_list(self):
        return self._time_range_list

    @time_range_list.setter
    def time_range_list(self, value):
        if isinstance(value, list):
            self._time_range_list = list()
            for i in value:
                if isinstance(i, KbdishTimeRangeInfo):
                    self._time_range_list.append(i)
                else:
                    self._time_range_list.append(KbdishTimeRangeInfo.from_alipay_dict(i))
    @property
    def weeks(self):
        return self._weeks

    @weeks.setter
    def weeks(self, value):
        self._weeks = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.time_range_list:
            if isinstance(self.time_range_list, list):
                for i in range(0, len(self.time_range_list)):
                    element = self.time_range_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.time_range_list[i] = element.to_alipay_dict()
            if hasattr(self.time_range_list, 'to_alipay_dict'):
                params['time_range_list'] = self.time_range_list.to_alipay_dict()
            else:
                params['time_range_list'] = self.time_range_list
        if self.weeks:
            if hasattr(self.weeks, 'to_alipay_dict'):
                params['weeks'] = self.weeks.to_alipay_dict()
            else:
                params['weeks'] = self.weeks
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishPeriodExtendInfo()
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'time_range_list' in d:
            o.time_range_list = d['time_range_list']
        if 'weeks' in d:
            o.weeks = d['weeks']
        return o


