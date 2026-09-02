#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ScheduleStationVO(object):

    def __init__(self):
        self._est_time_in_sec = None
        self._name = None
        self._order = None
        self._station_code = None
        self._train_stop_time = None

    @property
    def est_time_in_sec(self):
        return self._est_time_in_sec

    @est_time_in_sec.setter
    def est_time_in_sec(self, value):
        self._est_time_in_sec = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, value):
        self._order = value
    @property
    def station_code(self):
        return self._station_code

    @station_code.setter
    def station_code(self, value):
        self._station_code = value
    @property
    def train_stop_time(self):
        return self._train_stop_time

    @train_stop_time.setter
    def train_stop_time(self, value):
        self._train_stop_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.est_time_in_sec:
            if hasattr(self.est_time_in_sec, 'to_alipay_dict'):
                params['est_time_in_sec'] = self.est_time_in_sec.to_alipay_dict()
            else:
                params['est_time_in_sec'] = self.est_time_in_sec
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.order:
            if hasattr(self.order, 'to_alipay_dict'):
                params['order'] = self.order.to_alipay_dict()
            else:
                params['order'] = self.order
        if self.station_code:
            if hasattr(self.station_code, 'to_alipay_dict'):
                params['station_code'] = self.station_code.to_alipay_dict()
            else:
                params['station_code'] = self.station_code
        if self.train_stop_time:
            if hasattr(self.train_stop_time, 'to_alipay_dict'):
                params['train_stop_time'] = self.train_stop_time.to_alipay_dict()
            else:
                params['train_stop_time'] = self.train_stop_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ScheduleStationVO()
        if 'est_time_in_sec' in d:
            o.est_time_in_sec = d['est_time_in_sec']
        if 'name' in d:
            o.name = d['name']
        if 'order' in d:
            o.order = d['order']
        if 'station_code' in d:
            o.station_code = d['station_code']
        if 'train_stop_time' in d:
            o.train_stop_time = d['train_stop_time']
        return o


