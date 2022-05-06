#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TaxiOrder(object):

    def __init__(self):
        self._business_order_no = None
        self._car_no = None
        self._driver_name = None
        self._driver_user_id = None
        self._end_trip_time = None
        self._start_trip_time = None
        self._tele_no = None

    @property
    def business_order_no(self):
        return self._business_order_no

    @business_order_no.setter
    def business_order_no(self, value):
        self._business_order_no = value
    @property
    def car_no(self):
        return self._car_no

    @car_no.setter
    def car_no(self, value):
        self._car_no = value
    @property
    def driver_name(self):
        return self._driver_name

    @driver_name.setter
    def driver_name(self, value):
        self._driver_name = value
    @property
    def driver_user_id(self):
        return self._driver_user_id

    @driver_user_id.setter
    def driver_user_id(self, value):
        self._driver_user_id = value
    @property
    def end_trip_time(self):
        return self._end_trip_time

    @end_trip_time.setter
    def end_trip_time(self, value):
        self._end_trip_time = value
    @property
    def start_trip_time(self):
        return self._start_trip_time

    @start_trip_time.setter
    def start_trip_time(self, value):
        self._start_trip_time = value
    @property
    def tele_no(self):
        return self._tele_no

    @tele_no.setter
    def tele_no(self, value):
        self._tele_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_order_no:
            if hasattr(self.business_order_no, 'to_alipay_dict'):
                params['business_order_no'] = self.business_order_no.to_alipay_dict()
            else:
                params['business_order_no'] = self.business_order_no
        if self.car_no:
            if hasattr(self.car_no, 'to_alipay_dict'):
                params['car_no'] = self.car_no.to_alipay_dict()
            else:
                params['car_no'] = self.car_no
        if self.driver_name:
            if hasattr(self.driver_name, 'to_alipay_dict'):
                params['driver_name'] = self.driver_name.to_alipay_dict()
            else:
                params['driver_name'] = self.driver_name
        if self.driver_user_id:
            if hasattr(self.driver_user_id, 'to_alipay_dict'):
                params['driver_user_id'] = self.driver_user_id.to_alipay_dict()
            else:
                params['driver_user_id'] = self.driver_user_id
        if self.end_trip_time:
            if hasattr(self.end_trip_time, 'to_alipay_dict'):
                params['end_trip_time'] = self.end_trip_time.to_alipay_dict()
            else:
                params['end_trip_time'] = self.end_trip_time
        if self.start_trip_time:
            if hasattr(self.start_trip_time, 'to_alipay_dict'):
                params['start_trip_time'] = self.start_trip_time.to_alipay_dict()
            else:
                params['start_trip_time'] = self.start_trip_time
        if self.tele_no:
            if hasattr(self.tele_no, 'to_alipay_dict'):
                params['tele_no'] = self.tele_no.to_alipay_dict()
            else:
                params['tele_no'] = self.tele_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TaxiOrder()
        if 'business_order_no' in d:
            o.business_order_no = d['business_order_no']
        if 'car_no' in d:
            o.car_no = d['car_no']
        if 'driver_name' in d:
            o.driver_name = d['driver_name']
        if 'driver_user_id' in d:
            o.driver_user_id = d['driver_user_id']
        if 'end_trip_time' in d:
            o.end_trip_time = d['end_trip_time']
        if 'start_trip_time' in d:
            o.start_trip_time = d['start_trip_time']
        if 'tele_no' in d:
            o.tele_no = d['tele_no']
        return o


