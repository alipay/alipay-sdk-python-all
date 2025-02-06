#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoyagerSegmentOfPassengersCancelledInfo(object):

    def __init__(self):
        self._arrive_city_code = None
        self._depart_city_code = None
        self._depart_time = None
        self._flight_no = None
        self._passenger_name = None

    @property
    def arrive_city_code(self):
        return self._arrive_city_code

    @arrive_city_code.setter
    def arrive_city_code(self, value):
        self._arrive_city_code = value
    @property
    def depart_city_code(self):
        return self._depart_city_code

    @depart_city_code.setter
    def depart_city_code(self, value):
        self._depart_city_code = value
    @property
    def depart_time(self):
        return self._depart_time

    @depart_time.setter
    def depart_time(self, value):
        self._depart_time = value
    @property
    def flight_no(self):
        return self._flight_no

    @flight_no.setter
    def flight_no(self, value):
        self._flight_no = value
    @property
    def passenger_name(self):
        return self._passenger_name

    @passenger_name.setter
    def passenger_name(self, value):
        self._passenger_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.arrive_city_code:
            if hasattr(self.arrive_city_code, 'to_alipay_dict'):
                params['arrive_city_code'] = self.arrive_city_code.to_alipay_dict()
            else:
                params['arrive_city_code'] = self.arrive_city_code
        if self.depart_city_code:
            if hasattr(self.depart_city_code, 'to_alipay_dict'):
                params['depart_city_code'] = self.depart_city_code.to_alipay_dict()
            else:
                params['depart_city_code'] = self.depart_city_code
        if self.depart_time:
            if hasattr(self.depart_time, 'to_alipay_dict'):
                params['depart_time'] = self.depart_time.to_alipay_dict()
            else:
                params['depart_time'] = self.depart_time
        if self.flight_no:
            if hasattr(self.flight_no, 'to_alipay_dict'):
                params['flight_no'] = self.flight_no.to_alipay_dict()
            else:
                params['flight_no'] = self.flight_no
        if self.passenger_name:
            if hasattr(self.passenger_name, 'to_alipay_dict'):
                params['passenger_name'] = self.passenger_name.to_alipay_dict()
            else:
                params['passenger_name'] = self.passenger_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoyagerSegmentOfPassengersCancelledInfo()
        if 'arrive_city_code' in d:
            o.arrive_city_code = d['arrive_city_code']
        if 'depart_city_code' in d:
            o.depart_city_code = d['depart_city_code']
        if 'depart_time' in d:
            o.depart_time = d['depart_time']
        if 'flight_no' in d:
            o.flight_no = d['flight_no']
        if 'passenger_name' in d:
            o.passenger_name = d['passenger_name']
        return o


