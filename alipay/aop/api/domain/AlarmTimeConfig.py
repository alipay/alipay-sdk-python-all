#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlarmTimeConfig(object):

    def __init__(self):
        self._from = None
        self._time_type = None
        self._to = None
        self._weeks = None

    @property
    def from(self):
        return self._from

    @from.setter
    def from(self, value):
        self._from = value
    @property
    def time_type(self):
        return self._time_type

    @time_type.setter
    def time_type(self, value):
        self._time_type = value
    @property
    def to(self):
        return self._to

    @to.setter
    def to(self, value):
        self._to = value
    @property
    def weeks(self):
        return self._weeks

    @weeks.setter
    def weeks(self, value):
        if isinstance(value, list):
            self._weeks = list()
            for i in value:
                self._weeks.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.from:
            if hasattr(self.from, 'to_alipay_dict'):
                params['from'] = self.from.to_alipay_dict()
            else:
                params['from'] = self.from
        if self.time_type:
            if hasattr(self.time_type, 'to_alipay_dict'):
                params['time_type'] = self.time_type.to_alipay_dict()
            else:
                params['time_type'] = self.time_type
        if self.to:
            if hasattr(self.to, 'to_alipay_dict'):
                params['to'] = self.to.to_alipay_dict()
            else:
                params['to'] = self.to
        if self.weeks:
            if isinstance(self.weeks, list):
                for i in range(0, len(self.weeks)):
                    element = self.weeks[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.weeks[i] = element.to_alipay_dict()
            if hasattr(self.weeks, 'to_alipay_dict'):
                params['weeks'] = self.weeks.to_alipay_dict()
            else:
                params['weeks'] = self.weeks
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlarmTimeConfig()
        if 'from' in d:
            o.from = d['from']
        if 'time_type' in d:
            o.time_type = d['time_type']
        if 'to' in d:
            o.to = d['to']
        if 'weeks' in d:
            o.weeks = d['weeks']
        return o


