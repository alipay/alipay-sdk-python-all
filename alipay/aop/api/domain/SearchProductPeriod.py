#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SearchProductPeriod(object):

    def __init__(self):
        self._end_date = None
        self._start_date = None
        self._working_hours = None
        self._working_weekdays = None

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
    def working_hours(self):
        return self._working_hours

    @working_hours.setter
    def working_hours(self, value):
        if isinstance(value, list):
            self._working_hours = list()
            for i in value:
                self._working_hours.append(i)
    @property
    def working_weekdays(self):
        return self._working_weekdays

    @working_weekdays.setter
    def working_weekdays(self, value):
        if isinstance(value, list):
            self._working_weekdays = list()
            for i in value:
                self._working_weekdays.append(i)


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
        if self.working_hours:
            if isinstance(self.working_hours, list):
                for i in range(0, len(self.working_hours)):
                    element = self.working_hours[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.working_hours[i] = element.to_alipay_dict()
            if hasattr(self.working_hours, 'to_alipay_dict'):
                params['working_hours'] = self.working_hours.to_alipay_dict()
            else:
                params['working_hours'] = self.working_hours
        if self.working_weekdays:
            if isinstance(self.working_weekdays, list):
                for i in range(0, len(self.working_weekdays)):
                    element = self.working_weekdays[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.working_weekdays[i] = element.to_alipay_dict()
            if hasattr(self.working_weekdays, 'to_alipay_dict'):
                params['working_weekdays'] = self.working_weekdays.to_alipay_dict()
            else:
                params['working_weekdays'] = self.working_weekdays
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SearchProductPeriod()
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'working_hours' in d:
            o.working_hours = d['working_hours']
        if 'working_weekdays' in d:
            o.working_weekdays = d['working_weekdays']
        return o


