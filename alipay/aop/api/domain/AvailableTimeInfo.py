#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AvailableTimeInfo(object):

    def __init__(self):
        self._available_days = None
        self._from_time = None
        self._limit_period_unit = None
        self._to_time = None

    @property
    def available_days(self):
        return self._available_days

    @available_days.setter
    def available_days(self, value):
        if isinstance(value, list):
            self._available_days = list()
            for i in value:
                self._available_days.append(i)
    @property
    def from_time(self):
        return self._from_time

    @from_time.setter
    def from_time(self, value):
        self._from_time = value
    @property
    def limit_period_unit(self):
        return self._limit_period_unit

    @limit_period_unit.setter
    def limit_period_unit(self, value):
        self._limit_period_unit = value
    @property
    def to_time(self):
        return self._to_time

    @to_time.setter
    def to_time(self, value):
        self._to_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.available_days:
            if isinstance(self.available_days, list):
                for i in range(0, len(self.available_days)):
                    element = self.available_days[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.available_days[i] = element.to_alipay_dict()
            if hasattr(self.available_days, 'to_alipay_dict'):
                params['available_days'] = self.available_days.to_alipay_dict()
            else:
                params['available_days'] = self.available_days
        if self.from_time:
            if hasattr(self.from_time, 'to_alipay_dict'):
                params['from_time'] = self.from_time.to_alipay_dict()
            else:
                params['from_time'] = self.from_time
        if self.limit_period_unit:
            if hasattr(self.limit_period_unit, 'to_alipay_dict'):
                params['limit_period_unit'] = self.limit_period_unit.to_alipay_dict()
            else:
                params['limit_period_unit'] = self.limit_period_unit
        if self.to_time:
            if hasattr(self.to_time, 'to_alipay_dict'):
                params['to_time'] = self.to_time.to_alipay_dict()
            else:
                params['to_time'] = self.to_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AvailableTimeInfo()
        if 'available_days' in d:
            o.available_days = d['available_days']
        if 'from_time' in d:
            o.from_time = d['from_time']
        if 'limit_period_unit' in d:
            o.limit_period_unit = d['limit_period_unit']
        if 'to_time' in d:
            o.to_time = d['to_time']
        return o


