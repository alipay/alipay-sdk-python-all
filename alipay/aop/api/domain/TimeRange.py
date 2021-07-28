#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TimeRange(object):

    def __init__(self):
        self._begin = None
        self._end = None

    @property
    def begin(self):
        return self._begin

    @begin.setter
    def begin(self, value):
        self._begin = value
    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        self._end = value


    def to_alipay_dict(self):
        params = dict()
        if self.begin:
            if hasattr(self.begin, 'to_alipay_dict'):
                params['begin'] = self.begin.to_alipay_dict()
            else:
                params['begin'] = self.begin
        if self.end:
            if hasattr(self.end, 'to_alipay_dict'):
                params['end'] = self.end.to_alipay_dict()
            else:
                params['end'] = self.end
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TimeRange()
        if 'begin' in d:
            o.begin = d['begin']
        if 'end' in d:
            o.end = d['end']
        return o


