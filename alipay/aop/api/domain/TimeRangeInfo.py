#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EndTimeInfo import EndTimeInfo


class TimeRangeInfo(object):

    def __init__(self):
        self._begin_time = None
        self._end_time_info = None

    @property
    def begin_time(self):
        return self._begin_time

    @begin_time.setter
    def begin_time(self, value):
        self._begin_time = value
    @property
    def end_time_info(self):
        return self._end_time_info

    @end_time_info.setter
    def end_time_info(self, value):
        if isinstance(value, EndTimeInfo):
            self._end_time_info = value
        else:
            self._end_time_info = EndTimeInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.begin_time:
            if hasattr(self.begin_time, 'to_alipay_dict'):
                params['begin_time'] = self.begin_time.to_alipay_dict()
            else:
                params['begin_time'] = self.begin_time
        if self.end_time_info:
            if hasattr(self.end_time_info, 'to_alipay_dict'):
                params['end_time_info'] = self.end_time_info.to_alipay_dict()
            else:
                params['end_time_info'] = self.end_time_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TimeRangeInfo()
        if 'begin_time' in d:
            o.begin_time = d['begin_time']
        if 'end_time_info' in d:
            o.end_time_info = d['end_time_info']
        return o


