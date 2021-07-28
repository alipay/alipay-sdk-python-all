#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KmsBakingCheckDTO(object):

    def __init__(self):
        self._end_time = None
        self._start_time = None
        self._sync_count = None
        self._sync_time = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def sync_count(self):
        return self._sync_count

    @sync_count.setter
    def sync_count(self, value):
        self._sync_count = value
    @property
    def sync_time(self):
        return self._sync_time

    @sync_time.setter
    def sync_time(self, value):
        self._sync_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.sync_count:
            if hasattr(self.sync_count, 'to_alipay_dict'):
                params['sync_count'] = self.sync_count.to_alipay_dict()
            else:
                params['sync_count'] = self.sync_count
        if self.sync_time:
            if hasattr(self.sync_time, 'to_alipay_dict'):
                params['sync_time'] = self.sync_time.to_alipay_dict()
            else:
                params['sync_time'] = self.sync_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KmsBakingCheckDTO()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'sync_count' in d:
            o.sync_count = d['sync_count']
        if 'sync_time' in d:
            o.sync_time = d['sync_time']
        return o


