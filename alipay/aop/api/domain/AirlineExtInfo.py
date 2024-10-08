#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AirlineExtInfo(object):

    def __init__(self):
        self._arr_on_time = None
        self._avg_arr_delay = None
        self._avg_dep_delay = None
        self._cancel_pt = None
        self._charging_port = None
        self._covered_bridge = None
        self._dep_on_time = None
        self._tv = None
        self._wifi = None

    @property
    def arr_on_time(self):
        return self._arr_on_time

    @arr_on_time.setter
    def arr_on_time(self, value):
        self._arr_on_time = value
    @property
    def avg_arr_delay(self):
        return self._avg_arr_delay

    @avg_arr_delay.setter
    def avg_arr_delay(self, value):
        self._avg_arr_delay = value
    @property
    def avg_dep_delay(self):
        return self._avg_dep_delay

    @avg_dep_delay.setter
    def avg_dep_delay(self, value):
        self._avg_dep_delay = value
    @property
    def cancel_pt(self):
        return self._cancel_pt

    @cancel_pt.setter
    def cancel_pt(self, value):
        self._cancel_pt = value
    @property
    def charging_port(self):
        return self._charging_port

    @charging_port.setter
    def charging_port(self, value):
        self._charging_port = value
    @property
    def covered_bridge(self):
        return self._covered_bridge

    @covered_bridge.setter
    def covered_bridge(self, value):
        self._covered_bridge = value
    @property
    def dep_on_time(self):
        return self._dep_on_time

    @dep_on_time.setter
    def dep_on_time(self, value):
        self._dep_on_time = value
    @property
    def tv(self):
        return self._tv

    @tv.setter
    def tv(self, value):
        self._tv = value
    @property
    def wifi(self):
        return self._wifi

    @wifi.setter
    def wifi(self, value):
        self._wifi = value


    def to_alipay_dict(self):
        params = dict()
        if self.arr_on_time:
            if hasattr(self.arr_on_time, 'to_alipay_dict'):
                params['arr_on_time'] = self.arr_on_time.to_alipay_dict()
            else:
                params['arr_on_time'] = self.arr_on_time
        if self.avg_arr_delay:
            if hasattr(self.avg_arr_delay, 'to_alipay_dict'):
                params['avg_arr_delay'] = self.avg_arr_delay.to_alipay_dict()
            else:
                params['avg_arr_delay'] = self.avg_arr_delay
        if self.avg_dep_delay:
            if hasattr(self.avg_dep_delay, 'to_alipay_dict'):
                params['avg_dep_delay'] = self.avg_dep_delay.to_alipay_dict()
            else:
                params['avg_dep_delay'] = self.avg_dep_delay
        if self.cancel_pt:
            if hasattr(self.cancel_pt, 'to_alipay_dict'):
                params['cancel_pt'] = self.cancel_pt.to_alipay_dict()
            else:
                params['cancel_pt'] = self.cancel_pt
        if self.charging_port:
            if hasattr(self.charging_port, 'to_alipay_dict'):
                params['charging_port'] = self.charging_port.to_alipay_dict()
            else:
                params['charging_port'] = self.charging_port
        if self.covered_bridge:
            if hasattr(self.covered_bridge, 'to_alipay_dict'):
                params['covered_bridge'] = self.covered_bridge.to_alipay_dict()
            else:
                params['covered_bridge'] = self.covered_bridge
        if self.dep_on_time:
            if hasattr(self.dep_on_time, 'to_alipay_dict'):
                params['dep_on_time'] = self.dep_on_time.to_alipay_dict()
            else:
                params['dep_on_time'] = self.dep_on_time
        if self.tv:
            if hasattr(self.tv, 'to_alipay_dict'):
                params['tv'] = self.tv.to_alipay_dict()
            else:
                params['tv'] = self.tv
        if self.wifi:
            if hasattr(self.wifi, 'to_alipay_dict'):
                params['wifi'] = self.wifi.to_alipay_dict()
            else:
                params['wifi'] = self.wifi
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AirlineExtInfo()
        if 'arr_on_time' in d:
            o.arr_on_time = d['arr_on_time']
        if 'avg_arr_delay' in d:
            o.avg_arr_delay = d['avg_arr_delay']
        if 'avg_dep_delay' in d:
            o.avg_dep_delay = d['avg_dep_delay']
        if 'cancel_pt' in d:
            o.cancel_pt = d['cancel_pt']
        if 'charging_port' in d:
            o.charging_port = d['charging_port']
        if 'covered_bridge' in d:
            o.covered_bridge = d['covered_bridge']
        if 'dep_on_time' in d:
            o.dep_on_time = d['dep_on_time']
        if 'tv' in d:
            o.tv = d['tv']
        if 'wifi' in d:
            o.wifi = d['wifi']
        return o


