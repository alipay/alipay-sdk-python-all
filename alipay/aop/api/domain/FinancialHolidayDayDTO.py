#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FinancialHolidayDayDTO(object):

    def __init__(self):
        self._day = None
        self._day_of_week = None
        self._day_type = None
        self._event_name = None
        self._gmt_modified = None
        self._month = None
        self._year = None

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        self._day = value
    @property
    def day_of_week(self):
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, value):
        self._day_of_week = value
    @property
    def day_type(self):
        return self._day_type

    @day_type.setter
    def day_type(self, value):
        self._day_type = value
    @property
    def event_name(self):
        return self._event_name

    @event_name.setter
    def event_name(self, value):
        self._event_name = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        self._month = value
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value


    def to_alipay_dict(self):
        params = dict()
        if self.day:
            if hasattr(self.day, 'to_alipay_dict'):
                params['day'] = self.day.to_alipay_dict()
            else:
                params['day'] = self.day
        if self.day_of_week:
            if hasattr(self.day_of_week, 'to_alipay_dict'):
                params['day_of_week'] = self.day_of_week.to_alipay_dict()
            else:
                params['day_of_week'] = self.day_of_week
        if self.day_type:
            if hasattr(self.day_type, 'to_alipay_dict'):
                params['day_type'] = self.day_type.to_alipay_dict()
            else:
                params['day_type'] = self.day_type
        if self.event_name:
            if hasattr(self.event_name, 'to_alipay_dict'):
                params['event_name'] = self.event_name.to_alipay_dict()
            else:
                params['event_name'] = self.event_name
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.month:
            if hasattr(self.month, 'to_alipay_dict'):
                params['month'] = self.month.to_alipay_dict()
            else:
                params['month'] = self.month
        if self.year:
            if hasattr(self.year, 'to_alipay_dict'):
                params['year'] = self.year.to_alipay_dict()
            else:
                params['year'] = self.year
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FinancialHolidayDayDTO()
        if 'day' in d:
            o.day = d['day']
        if 'day_of_week' in d:
            o.day_of_week = d['day_of_week']
        if 'day_type' in d:
            o.day_type = d['day_type']
        if 'event_name' in d:
            o.event_name = d['event_name']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'month' in d:
            o.month = d['month']
        if 'year' in d:
            o.year = d['year']
        return o


