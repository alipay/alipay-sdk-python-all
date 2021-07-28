#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FrequencyRuleDetail(object):

    def __init__(self):
        self._frequency_duration = None
        self._frequency_type = None
        self._total_times = None
        self._used_times = None

    @property
    def frequency_duration(self):
        return self._frequency_duration

    @frequency_duration.setter
    def frequency_duration(self, value):
        self._frequency_duration = value
    @property
    def frequency_type(self):
        return self._frequency_type

    @frequency_type.setter
    def frequency_type(self, value):
        self._frequency_type = value
    @property
    def total_times(self):
        return self._total_times

    @total_times.setter
    def total_times(self, value):
        self._total_times = value
    @property
    def used_times(self):
        return self._used_times

    @used_times.setter
    def used_times(self, value):
        self._used_times = value


    def to_alipay_dict(self):
        params = dict()
        if self.frequency_duration:
            if hasattr(self.frequency_duration, 'to_alipay_dict'):
                params['frequency_duration'] = self.frequency_duration.to_alipay_dict()
            else:
                params['frequency_duration'] = self.frequency_duration
        if self.frequency_type:
            if hasattr(self.frequency_type, 'to_alipay_dict'):
                params['frequency_type'] = self.frequency_type.to_alipay_dict()
            else:
                params['frequency_type'] = self.frequency_type
        if self.total_times:
            if hasattr(self.total_times, 'to_alipay_dict'):
                params['total_times'] = self.total_times.to_alipay_dict()
            else:
                params['total_times'] = self.total_times
        if self.used_times:
            if hasattr(self.used_times, 'to_alipay_dict'):
                params['used_times'] = self.used_times.to_alipay_dict()
            else:
                params['used_times'] = self.used_times
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FrequencyRuleDetail()
        if 'frequency_duration' in d:
            o.frequency_duration = d['frequency_duration']
        if 'frequency_type' in d:
            o.frequency_type = d['frequency_type']
        if 'total_times' in d:
            o.total_times = d['total_times']
        if 'used_times' in d:
            o.used_times = d['used_times']
        return o


