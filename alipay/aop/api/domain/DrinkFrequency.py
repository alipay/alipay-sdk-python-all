#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DrinkFrequency(object):

    def __init__(self):
        self._frequency = None
        self._time = None
        self._time_unit = None

    @property
    def frequency(self):
        return self._frequency

    @frequency.setter
    def frequency(self, value):
        self._frequency = value
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value
    @property
    def time_unit(self):
        return self._time_unit

    @time_unit.setter
    def time_unit(self, value):
        self._time_unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.frequency:
            if hasattr(self.frequency, 'to_alipay_dict'):
                params['frequency'] = self.frequency.to_alipay_dict()
            else:
                params['frequency'] = self.frequency
        if self.time:
            if hasattr(self.time, 'to_alipay_dict'):
                params['time'] = self.time.to_alipay_dict()
            else:
                params['time'] = self.time
        if self.time_unit:
            if hasattr(self.time_unit, 'to_alipay_dict'):
                params['time_unit'] = self.time_unit.to_alipay_dict()
            else:
                params['time_unit'] = self.time_unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DrinkFrequency()
        if 'frequency' in d:
            o.frequency = d['frequency']
        if 'time' in d:
            o.time = d['time']
        if 'time_unit' in d:
            o.time_unit = d['time_unit']
        return o


