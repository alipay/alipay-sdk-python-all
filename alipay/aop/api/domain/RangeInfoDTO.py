#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RangeInfoDTO(object):

    def __init__(self):
        self._available = None
        self._date_type = None
        self._end_time = None
        self._immediately = None
        self._start_time = None

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, value):
        self._available = value
    @property
    def date_type(self):
        return self._date_type

    @date_type.setter
    def date_type(self, value):
        self._date_type = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def immediately(self):
        return self._immediately

    @immediately.setter
    def immediately(self, value):
        self._immediately = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.available:
            if hasattr(self.available, 'to_alipay_dict'):
                params['available'] = self.available.to_alipay_dict()
            else:
                params['available'] = self.available
        if self.date_type:
            if hasattr(self.date_type, 'to_alipay_dict'):
                params['date_type'] = self.date_type.to_alipay_dict()
            else:
                params['date_type'] = self.date_type
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.immediately:
            if hasattr(self.immediately, 'to_alipay_dict'):
                params['immediately'] = self.immediately.to_alipay_dict()
            else:
                params['immediately'] = self.immediately
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
        o = RangeInfoDTO()
        if 'available' in d:
            o.available = d['available']
        if 'date_type' in d:
            o.date_type = d['date_type']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'immediately' in d:
            o.immediately = d['immediately']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


