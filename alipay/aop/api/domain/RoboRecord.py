#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RoboRecord(object):

    def __init__(self):
        self._arrive_dest_time = None
        self._begin_charge_time = None
        self._driver_reach_time = None
        self._driver_server_time = None

    @property
    def arrive_dest_time(self):
        return self._arrive_dest_time

    @arrive_dest_time.setter
    def arrive_dest_time(self, value):
        self._arrive_dest_time = value
    @property
    def begin_charge_time(self):
        return self._begin_charge_time

    @begin_charge_time.setter
    def begin_charge_time(self, value):
        self._begin_charge_time = value
    @property
    def driver_reach_time(self):
        return self._driver_reach_time

    @driver_reach_time.setter
    def driver_reach_time(self, value):
        self._driver_reach_time = value
    @property
    def driver_server_time(self):
        return self._driver_server_time

    @driver_server_time.setter
    def driver_server_time(self, value):
        self._driver_server_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.arrive_dest_time:
            if hasattr(self.arrive_dest_time, 'to_alipay_dict'):
                params['arrive_dest_time'] = self.arrive_dest_time.to_alipay_dict()
            else:
                params['arrive_dest_time'] = self.arrive_dest_time
        if self.begin_charge_time:
            if hasattr(self.begin_charge_time, 'to_alipay_dict'):
                params['begin_charge_time'] = self.begin_charge_time.to_alipay_dict()
            else:
                params['begin_charge_time'] = self.begin_charge_time
        if self.driver_reach_time:
            if hasattr(self.driver_reach_time, 'to_alipay_dict'):
                params['driver_reach_time'] = self.driver_reach_time.to_alipay_dict()
            else:
                params['driver_reach_time'] = self.driver_reach_time
        if self.driver_server_time:
            if hasattr(self.driver_server_time, 'to_alipay_dict'):
                params['driver_server_time'] = self.driver_server_time.to_alipay_dict()
            else:
                params['driver_server_time'] = self.driver_server_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RoboRecord()
        if 'arrive_dest_time' in d:
            o.arrive_dest_time = d['arrive_dest_time']
        if 'begin_charge_time' in d:
            o.begin_charge_time = d['begin_charge_time']
        if 'driver_reach_time' in d:
            o.driver_reach_time = d['driver_reach_time']
        if 'driver_server_time' in d:
            o.driver_server_time = d['driver_server_time']
        return o


