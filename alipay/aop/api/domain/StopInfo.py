#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StopInfo(object):

    def __init__(self):
        self._stop_airport = None
        self._stop_airport_name = None
        self._stop_city = None
        self._stop_city_name = None
        self._stop_time = None

    @property
    def stop_airport(self):
        return self._stop_airport

    @stop_airport.setter
    def stop_airport(self, value):
        self._stop_airport = value
    @property
    def stop_airport_name(self):
        return self._stop_airport_name

    @stop_airport_name.setter
    def stop_airport_name(self, value):
        self._stop_airport_name = value
    @property
    def stop_city(self):
        return self._stop_city

    @stop_city.setter
    def stop_city(self, value):
        self._stop_city = value
    @property
    def stop_city_name(self):
        return self._stop_city_name

    @stop_city_name.setter
    def stop_city_name(self, value):
        self._stop_city_name = value
    @property
    def stop_time(self):
        return self._stop_time

    @stop_time.setter
    def stop_time(self, value):
        self._stop_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.stop_airport:
            if hasattr(self.stop_airport, 'to_alipay_dict'):
                params['stop_airport'] = self.stop_airport.to_alipay_dict()
            else:
                params['stop_airport'] = self.stop_airport
        if self.stop_airport_name:
            if hasattr(self.stop_airport_name, 'to_alipay_dict'):
                params['stop_airport_name'] = self.stop_airport_name.to_alipay_dict()
            else:
                params['stop_airport_name'] = self.stop_airport_name
        if self.stop_city:
            if hasattr(self.stop_city, 'to_alipay_dict'):
                params['stop_city'] = self.stop_city.to_alipay_dict()
            else:
                params['stop_city'] = self.stop_city
        if self.stop_city_name:
            if hasattr(self.stop_city_name, 'to_alipay_dict'):
                params['stop_city_name'] = self.stop_city_name.to_alipay_dict()
            else:
                params['stop_city_name'] = self.stop_city_name
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
        o = StopInfo()
        if 'stop_airport' in d:
            o.stop_airport = d['stop_airport']
        if 'stop_airport_name' in d:
            o.stop_airport_name = d['stop_airport_name']
        if 'stop_city' in d:
            o.stop_city = d['stop_city']
        if 'stop_city_name' in d:
            o.stop_city_name = d['stop_city_name']
        if 'stop_time' in d:
            o.stop_time = d['stop_time']
        return o


