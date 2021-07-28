#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InputScheduleTime(object):

    def __init__(self):
        self._capacity = None
        self._direction = None
        self._exp_trip_cnt = None
        self._ext_param = None
        self._line_id = None

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._capacity = value
    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value
    @property
    def exp_trip_cnt(self):
        return self._exp_trip_cnt

    @exp_trip_cnt.setter
    def exp_trip_cnt(self, value):
        self._exp_trip_cnt = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def line_id(self):
        return self._line_id

    @line_id.setter
    def line_id(self, value):
        self._line_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.capacity:
            if hasattr(self.capacity, 'to_alipay_dict'):
                params['capacity'] = self.capacity.to_alipay_dict()
            else:
                params['capacity'] = self.capacity
        if self.direction:
            if hasattr(self.direction, 'to_alipay_dict'):
                params['direction'] = self.direction.to_alipay_dict()
            else:
                params['direction'] = self.direction
        if self.exp_trip_cnt:
            if hasattr(self.exp_trip_cnt, 'to_alipay_dict'):
                params['exp_trip_cnt'] = self.exp_trip_cnt.to_alipay_dict()
            else:
                params['exp_trip_cnt'] = self.exp_trip_cnt
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.line_id:
            if hasattr(self.line_id, 'to_alipay_dict'):
                params['line_id'] = self.line_id.to_alipay_dict()
            else:
                params['line_id'] = self.line_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InputScheduleTime()
        if 'capacity' in d:
            o.capacity = d['capacity']
        if 'direction' in d:
            o.direction = d['direction']
        if 'exp_trip_cnt' in d:
            o.exp_trip_cnt = d['exp_trip_cnt']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'line_id' in d:
            o.line_id = d['line_id']
        return o


