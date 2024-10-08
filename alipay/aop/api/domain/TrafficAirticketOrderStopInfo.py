#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TrafficAirticketOrderStopInfo(object):

    def __init__(self):
        self._stop_airport_code = None
        self._stop_airport_name = None
        self._stop_arr_time = None
        self._stop_city_code = None
        self._stop_city_name = None
        self._stop_dep_time = None
        self._stop_time = None

    @property
    def stop_airport_code(self):
        return self._stop_airport_code

    @stop_airport_code.setter
    def stop_airport_code(self, value):
        self._stop_airport_code = value
    @property
    def stop_airport_name(self):
        return self._stop_airport_name

    @stop_airport_name.setter
    def stop_airport_name(self, value):
        self._stop_airport_name = value
    @property
    def stop_arr_time(self):
        return self._stop_arr_time

    @stop_arr_time.setter
    def stop_arr_time(self, value):
        self._stop_arr_time = value
    @property
    def stop_city_code(self):
        return self._stop_city_code

    @stop_city_code.setter
    def stop_city_code(self, value):
        self._stop_city_code = value
    @property
    def stop_city_name(self):
        return self._stop_city_name

    @stop_city_name.setter
    def stop_city_name(self, value):
        self._stop_city_name = value
    @property
    def stop_dep_time(self):
        return self._stop_dep_time

    @stop_dep_time.setter
    def stop_dep_time(self, value):
        self._stop_dep_time = value
    @property
    def stop_time(self):
        return self._stop_time

    @stop_time.setter
    def stop_time(self, value):
        self._stop_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.stop_airport_code:
            if hasattr(self.stop_airport_code, 'to_alipay_dict'):
                params['stop_airport_code'] = self.stop_airport_code.to_alipay_dict()
            else:
                params['stop_airport_code'] = self.stop_airport_code
        if self.stop_airport_name:
            if hasattr(self.stop_airport_name, 'to_alipay_dict'):
                params['stop_airport_name'] = self.stop_airport_name.to_alipay_dict()
            else:
                params['stop_airport_name'] = self.stop_airport_name
        if self.stop_arr_time:
            if hasattr(self.stop_arr_time, 'to_alipay_dict'):
                params['stop_arr_time'] = self.stop_arr_time.to_alipay_dict()
            else:
                params['stop_arr_time'] = self.stop_arr_time
        if self.stop_city_code:
            if hasattr(self.stop_city_code, 'to_alipay_dict'):
                params['stop_city_code'] = self.stop_city_code.to_alipay_dict()
            else:
                params['stop_city_code'] = self.stop_city_code
        if self.stop_city_name:
            if hasattr(self.stop_city_name, 'to_alipay_dict'):
                params['stop_city_name'] = self.stop_city_name.to_alipay_dict()
            else:
                params['stop_city_name'] = self.stop_city_name
        if self.stop_dep_time:
            if hasattr(self.stop_dep_time, 'to_alipay_dict'):
                params['stop_dep_time'] = self.stop_dep_time.to_alipay_dict()
            else:
                params['stop_dep_time'] = self.stop_dep_time
        if self.stop_time:
            if hasattr(self.stop_time, 'to_alipay_dict'):
                params['stop_time'] = self.stop_time.to_alipay_dict()
            else:
                params['stop_time'] = self.stop_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TrafficAirticketOrderStopInfo()
        if 'stop_airport_code' in d:
            o.stop_airport_code = d['stop_airport_code']
        if 'stop_airport_name' in d:
            o.stop_airport_name = d['stop_airport_name']
        if 'stop_arr_time' in d:
            o.stop_arr_time = d['stop_arr_time']
        if 'stop_city_code' in d:
            o.stop_city_code = d['stop_city_code']
        if 'stop_city_name' in d:
            o.stop_city_name = d['stop_city_name']
        if 'stop_dep_time' in d:
            o.stop_dep_time = d['stop_dep_time']
        if 'stop_time' in d:
            o.stop_time = d['stop_time']
        return o


