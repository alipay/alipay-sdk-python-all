#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DtBankCouponAvailableTime(object):

    def __init__(self):
        self._absolutely_begin_time = None
        self._absolutely_end_time = None
        self._relative_available_time = None
        self._relative_begin_time_type = None
        self._time_type = None

    @property
    def absolutely_begin_time(self):
        return self._absolutely_begin_time

    @absolutely_begin_time.setter
    def absolutely_begin_time(self, value):
        self._absolutely_begin_time = value
    @property
    def absolutely_end_time(self):
        return self._absolutely_end_time

    @absolutely_end_time.setter
    def absolutely_end_time(self, value):
        self._absolutely_end_time = value
    @property
    def relative_available_time(self):
        return self._relative_available_time

    @relative_available_time.setter
    def relative_available_time(self, value):
        self._relative_available_time = value
    @property
    def relative_begin_time_type(self):
        return self._relative_begin_time_type

    @relative_begin_time_type.setter
    def relative_begin_time_type(self, value):
        self._relative_begin_time_type = value
    @property
    def time_type(self):
        return self._time_type

    @time_type.setter
    def time_type(self, value):
        self._time_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.absolutely_begin_time:
            if hasattr(self.absolutely_begin_time, 'to_alipay_dict'):
                params['absolutely_begin_time'] = self.absolutely_begin_time.to_alipay_dict()
            else:
                params['absolutely_begin_time'] = self.absolutely_begin_time
        if self.absolutely_end_time:
            if hasattr(self.absolutely_end_time, 'to_alipay_dict'):
                params['absolutely_end_time'] = self.absolutely_end_time.to_alipay_dict()
            else:
                params['absolutely_end_time'] = self.absolutely_end_time
        if self.relative_available_time:
            if hasattr(self.relative_available_time, 'to_alipay_dict'):
                params['relative_available_time'] = self.relative_available_time.to_alipay_dict()
            else:
                params['relative_available_time'] = self.relative_available_time
        if self.relative_begin_time_type:
            if hasattr(self.relative_begin_time_type, 'to_alipay_dict'):
                params['relative_begin_time_type'] = self.relative_begin_time_type.to_alipay_dict()
            else:
                params['relative_begin_time_type'] = self.relative_begin_time_type
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
        o = DtBankCouponAvailableTime()
        if 'absolutely_begin_time' in d:
            o.absolutely_begin_time = d['absolutely_begin_time']
        if 'absolutely_end_time' in d:
            o.absolutely_end_time = d['absolutely_end_time']
        if 'relative_available_time' in d:
            o.relative_available_time = d['relative_available_time']
        if 'relative_begin_time_type' in d:
            o.relative_begin_time_type = d['relative_begin_time_type']
        if 'time_type' in d:
            o.time_type = d['time_type']
        return o


