#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MTimeControlInfo(object):

    def __init__(self):
        self._time_dimension_type = None
        self._times = None
        self._values = None

    @property
    def time_dimension_type(self):
        return self._time_dimension_type

    @time_dimension_type.setter
    def time_dimension_type(self, value):
        self._time_dimension_type = value
    @property
    def times(self):
        return self._times

    @times.setter
    def times(self, value):
        self._times = value
    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, value):
        self._values = value


    def to_alipay_dict(self):
        params = dict()
        if self.time_dimension_type:
            if hasattr(self.time_dimension_type, 'to_alipay_dict'):
                params['time_dimension_type'] = self.time_dimension_type.to_alipay_dict()
            else:
                params['time_dimension_type'] = self.time_dimension_type
        if self.times:
            if hasattr(self.times, 'to_alipay_dict'):
                params['times'] = self.times.to_alipay_dict()
            else:
                params['times'] = self.times
        if self.values:
            if hasattr(self.values, 'to_alipay_dict'):
                params['values'] = self.values.to_alipay_dict()
            else:
                params['values'] = self.values
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MTimeControlInfo()
        if 'time_dimension_type' in d:
            o.time_dimension_type = d['time_dimension_type']
        if 'times' in d:
            o.times = d['times']
        if 'values' in d:
            o.values = d['values']
        return o


