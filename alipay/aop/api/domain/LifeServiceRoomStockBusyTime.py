#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LifeServiceRoomStockBusyTime(object):

    def __init__(self):
        self._busy_reason = None
        self._busy_time_end = None
        self._busy_time_start = None

    @property
    def busy_reason(self):
        return self._busy_reason

    @busy_reason.setter
    def busy_reason(self, value):
        self._busy_reason = value
    @property
    def busy_time_end(self):
        return self._busy_time_end

    @busy_time_end.setter
    def busy_time_end(self, value):
        self._busy_time_end = value
    @property
    def busy_time_start(self):
        return self._busy_time_start

    @busy_time_start.setter
    def busy_time_start(self, value):
        self._busy_time_start = value


    def to_alipay_dict(self):
        params = dict()
        if self.busy_reason:
            if hasattr(self.busy_reason, 'to_alipay_dict'):
                params['busy_reason'] = self.busy_reason.to_alipay_dict()
            else:
                params['busy_reason'] = self.busy_reason
        if self.busy_time_end:
            if hasattr(self.busy_time_end, 'to_alipay_dict'):
                params['busy_time_end'] = self.busy_time_end.to_alipay_dict()
            else:
                params['busy_time_end'] = self.busy_time_end
        if self.busy_time_start:
            if hasattr(self.busy_time_start, 'to_alipay_dict'):
                params['busy_time_start'] = self.busy_time_start.to_alipay_dict()
            else:
                params['busy_time_start'] = self.busy_time_start
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LifeServiceRoomStockBusyTime()
        if 'busy_reason' in d:
            o.busy_reason = d['busy_reason']
        if 'busy_time_end' in d:
            o.busy_time_end = d['busy_time_end']
        if 'busy_time_start' in d:
            o.busy_time_start = d['busy_time_start']
        return o


