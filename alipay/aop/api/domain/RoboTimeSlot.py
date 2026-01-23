#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RoboTimeSlot(object):

    def __init__(self):
        self._end_time = None
        self._night_operate = None
        self._start_time = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def night_operate(self):
        return self._night_operate

    @night_operate.setter
    def night_operate(self, value):
        self._night_operate = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.night_operate:
            if hasattr(self.night_operate, 'to_alipay_dict'):
                params['night_operate'] = self.night_operate.to_alipay_dict()
            else:
                params['night_operate'] = self.night_operate
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RoboTimeSlot()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'night_operate' in d:
            o.night_operate = d['night_operate']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


