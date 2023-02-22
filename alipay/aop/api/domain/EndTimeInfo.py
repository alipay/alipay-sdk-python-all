#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EndTimeInfo(object):

    def __init__(self):
        self._end_time = None
        self._end_time_type = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def end_time_type(self):
        return self._end_time_type

    @end_time_type.setter
    def end_time_type(self, value):
        self._end_time_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.end_time_type:
            if hasattr(self.end_time_type, 'to_alipay_dict'):
                params['end_time_type'] = self.end_time_type.to_alipay_dict()
            else:
                params['end_time_type'] = self.end_time_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EndTimeInfo()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'end_time_type' in d:
            o.end_time_type = d['end_time_type']
        return o


