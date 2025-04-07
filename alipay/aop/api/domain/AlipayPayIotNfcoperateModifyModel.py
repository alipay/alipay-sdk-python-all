#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPayIotNfcoperateModifyModel(object):

    def __init__(self):
        self._end_time = None
        self._offline = None
        self._operator = None
        self._plan_id = None
        self._start_time = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def offline(self):
        return self._offline

    @offline.setter
    def offline(self, value):
        self._offline = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
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
        if self.offline:
            if hasattr(self.offline, 'to_alipay_dict'):
                params['offline'] = self.offline.to_alipay_dict()
            else:
                params['offline'] = self.offline
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
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
        o = AlipayPayIotNfcoperateModifyModel()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'offline' in d:
            o.offline = d['offline']
        if 'operator' in d:
            o.operator = d['operator']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


