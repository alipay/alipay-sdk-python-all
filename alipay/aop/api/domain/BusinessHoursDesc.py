#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BusinessHoursDesc(object):

    def __init__(self):
        self._days_in_week = None
        self._hours = None

    @property
    def days_in_week(self):
        return self._days_in_week

    @days_in_week.setter
    def days_in_week(self, value):
        if isinstance(value, list):
            self._days_in_week = list()
            for i in value:
                self._days_in_week.append(i)
    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, value):
        self._hours = value


    def to_alipay_dict(self):
        params = dict()
        if self.days_in_week:
            if isinstance(self.days_in_week, list):
                for i in range(0, len(self.days_in_week)):
                    element = self.days_in_week[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.days_in_week[i] = element.to_alipay_dict()
            if hasattr(self.days_in_week, 'to_alipay_dict'):
                params['days_in_week'] = self.days_in_week.to_alipay_dict()
            else:
                params['days_in_week'] = self.days_in_week
        if self.hours:
            if hasattr(self.hours, 'to_alipay_dict'):
                params['hours'] = self.hours.to_alipay_dict()
            else:
                params['hours'] = self.hours
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BusinessHoursDesc()
        if 'days_in_week' in d:
            o.days_in_week = d['days_in_week']
        if 'hours' in d:
            o.hours = d['hours']
        return o


