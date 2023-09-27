#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DateRangeDTO(object):

    def __init__(self):
        self._end = None
        self._start = None

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        self._end = value
    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        self._start = value


    def to_alipay_dict(self):
        params = dict()
        if self.end:
            if hasattr(self.end, 'to_alipay_dict'):
                params['end'] = self.end.to_alipay_dict()
            else:
                params['end'] = self.end
        if self.start:
            if hasattr(self.start, 'to_alipay_dict'):
                params['start'] = self.start.to_alipay_dict()
            else:
                params['start'] = self.start
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DateRangeDTO()
        if 'end' in d:
            o.end = d['end']
        if 'start' in d:
            o.start = d['start']
        return o


