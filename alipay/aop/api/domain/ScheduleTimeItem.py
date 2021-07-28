#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ScheduleTimeItem(object):

    def __init__(self):
        self._departure_time_list = None
        self._direction = None
        self._line_id = None
        self._occu_rate_sts = None
        self._trip_cnt = None
        self._wait_bus_sts = None
        self._wait_time_sts = None

    @property
    def departure_time_list(self):
        return self._departure_time_list

    @departure_time_list.setter
    def departure_time_list(self, value):
        self._departure_time_list = value
    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value
    @property
    def line_id(self):
        return self._line_id

    @line_id.setter
    def line_id(self, value):
        self._line_id = value
    @property
    def occu_rate_sts(self):
        return self._occu_rate_sts

    @occu_rate_sts.setter
    def occu_rate_sts(self, value):
        self._occu_rate_sts = value
    @property
    def trip_cnt(self):
        return self._trip_cnt

    @trip_cnt.setter
    def trip_cnt(self, value):
        self._trip_cnt = value
    @property
    def wait_bus_sts(self):
        return self._wait_bus_sts

    @wait_bus_sts.setter
    def wait_bus_sts(self, value):
        self._wait_bus_sts = value
    @property
    def wait_time_sts(self):
        return self._wait_time_sts

    @wait_time_sts.setter
    def wait_time_sts(self, value):
        self._wait_time_sts = value


    def to_alipay_dict(self):
        params = dict()
        if self.departure_time_list:
            if hasattr(self.departure_time_list, 'to_alipay_dict'):
                params['departure_time_list'] = self.departure_time_list.to_alipay_dict()
            else:
                params['departure_time_list'] = self.departure_time_list
        if self.direction:
            if hasattr(self.direction, 'to_alipay_dict'):
                params['direction'] = self.direction.to_alipay_dict()
            else:
                params['direction'] = self.direction
        if self.line_id:
            if hasattr(self.line_id, 'to_alipay_dict'):
                params['line_id'] = self.line_id.to_alipay_dict()
            else:
                params['line_id'] = self.line_id
        if self.occu_rate_sts:
            if hasattr(self.occu_rate_sts, 'to_alipay_dict'):
                params['occu_rate_sts'] = self.occu_rate_sts.to_alipay_dict()
            else:
                params['occu_rate_sts'] = self.occu_rate_sts
        if self.trip_cnt:
            if hasattr(self.trip_cnt, 'to_alipay_dict'):
                params['trip_cnt'] = self.trip_cnt.to_alipay_dict()
            else:
                params['trip_cnt'] = self.trip_cnt
        if self.wait_bus_sts:
            if hasattr(self.wait_bus_sts, 'to_alipay_dict'):
                params['wait_bus_sts'] = self.wait_bus_sts.to_alipay_dict()
            else:
                params['wait_bus_sts'] = self.wait_bus_sts
        if self.wait_time_sts:
            if hasattr(self.wait_time_sts, 'to_alipay_dict'):
                params['wait_time_sts'] = self.wait_time_sts.to_alipay_dict()
            else:
                params['wait_time_sts'] = self.wait_time_sts
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ScheduleTimeItem()
        if 'departure_time_list' in d:
            o.departure_time_list = d['departure_time_list']
        if 'direction' in d:
            o.direction = d['direction']
        if 'line_id' in d:
            o.line_id = d['line_id']
        if 'occu_rate_sts' in d:
            o.occu_rate_sts = d['occu_rate_sts']
        if 'trip_cnt' in d:
            o.trip_cnt = d['trip_cnt']
        if 'wait_bus_sts' in d:
            o.wait_bus_sts = d['wait_bus_sts']
        if 'wait_time_sts' in d:
            o.wait_time_sts = d['wait_time_sts']
        return o


