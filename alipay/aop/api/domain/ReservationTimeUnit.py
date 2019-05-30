#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReservationTimeUnit(object):

    def __init__(self):
        self._time = None
        self._time_type = None

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value
    @property
    def time_type(self):
        return self._time_type

    @time_type.setter
    def time_type(self, value):
        self._time_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.time:
            if hasattr(self.time, 'to_alipay_dict'):
                params['time'] = self.time.to_alipay_dict()
            else:
                params['time'] = self.time
        if self.time_type:
            if hasattr(self.time_type, 'to_alipay_dict'):
                params['time_type'] = self.time_type.to_alipay_dict()
            else:
                params['time_type'] = self.time_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReservationTimeUnit()
        if 'time' in d:
            o.time = d['time']
        if 'time_type' in d:
            o.time_type = d['time_type']
        return o


