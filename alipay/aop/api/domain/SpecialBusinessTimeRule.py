#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TimeRange import TimeRange


class SpecialBusinessTimeRule(object):

    def __init__(self):
        self._begin_date = None
        self._close_all_day = None
        self._end_date = None
        self._open_all_day = None
        self._open_time_list = None

    @property
    def begin_date(self):
        return self._begin_date

    @begin_date.setter
    def begin_date(self, value):
        self._begin_date = value
    @property
    def close_all_day(self):
        return self._close_all_day

    @close_all_day.setter
    def close_all_day(self, value):
        self._close_all_day = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def open_all_day(self):
        return self._open_all_day

    @open_all_day.setter
    def open_all_day(self, value):
        self._open_all_day = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.begin_date:
            if hasattr(self.begin_date, 'to_alipay_dict'):
                params['begin_date'] = self.begin_date.to_alipay_dict()
            else:
                params['begin_date'] = self.begin_date
        if self.close_all_day:
            if hasattr(self.close_all_day, 'to_alipay_dict'):
                params['close_all_day'] = self.close_all_day.to_alipay_dict()
            else:
                params['close_all_day'] = self.close_all_day
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.open_all_day:
            if hasattr(self.open_all_day, 'to_alipay_dict'):
                params['open_all_day'] = self.open_all_day.to_alipay_dict()
            else:
                params['open_all_day'] = self.open_all_day
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SpecialBusinessTimeRule()
        if 'begin_date' in d:
            o.begin_date = d['begin_date']
        if 'close_all_day' in d:
            o.close_all_day = d['close_all_day']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'open_all_day' in d:
            o.open_all_day = d['open_all_day']
        if 'open_time_list' in d:
            o.open_time_list = d['open_time_list']
        return o


