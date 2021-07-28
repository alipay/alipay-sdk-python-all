#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BusinessHoursInfo(object):

    def __init__(self):
        self._business_date = None
        self._end_time = None
        self._extra_desc = None
        self._start_time = None

    @property
    def business_date(self):
        return self._business_date

    @business_date.setter
    def business_date(self, value):
        if isinstance(value, list):
            self._business_date = list()
            for i in value:
                self._business_date.append(i)
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def extra_desc(self):
        return self._extra_desc

    @extra_desc.setter
    def extra_desc(self, value):
        self._extra_desc = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_date:
            if isinstance(self.business_date, list):
                for i in range(0, len(self.business_date)):
                    element = self.business_date[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.business_date[i] = element.to_alipay_dict()
            if hasattr(self.business_date, 'to_alipay_dict'):
                params['business_date'] = self.business_date.to_alipay_dict()
            else:
                params['business_date'] = self.business_date
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.extra_desc:
            if hasattr(self.extra_desc, 'to_alipay_dict'):
                params['extra_desc'] = self.extra_desc.to_alipay_dict()
            else:
                params['extra_desc'] = self.extra_desc
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
        o = BusinessHoursInfo()
        if 'business_date' in d:
            o.business_date = d['business_date']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'extra_desc' in d:
            o.extra_desc = d['extra_desc']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


