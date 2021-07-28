#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WorkPatternDetail(object):

    def __init__(self):
        self._end_time = None
        self._ext_param = None
        self._service_trip_count = None
        self._start_time = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def service_trip_count(self):
        return self._service_trip_count

    @service_trip_count.setter
    def service_trip_count(self, value):
        self._service_trip_count = value
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
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.service_trip_count:
            if hasattr(self.service_trip_count, 'to_alipay_dict'):
                params['service_trip_count'] = self.service_trip_count.to_alipay_dict()
            else:
                params['service_trip_count'] = self.service_trip_count
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
        o = WorkPatternDetail()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'service_trip_count' in d:
            o.service_trip_count = d['service_trip_count']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


