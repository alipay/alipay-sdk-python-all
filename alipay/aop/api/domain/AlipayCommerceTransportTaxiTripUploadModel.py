#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportTaxiTripUploadModel(object):

    def __init__(self):
        self._car_no = None
        self._driver_cert_no = None
        self._driver_name = None
        self._driver_sign_in_time = None
        self._extra_amount = None
        self._has_standby_driver = None
        self._low_speed_wait_time = None
        self._machine_sn = None
        self._order_amount = None
        self._reserve = None
        self._trip_amount = None
        self._trip_cost_time = None
        self._trip_end_location = None
        self._trip_end_time = None
        self._trip_id = None
        self._trip_mileage = None
        self._trip_start_location = None
        self._trip_start_time = None
        self._trip_type = None

    @property
    def car_no(self):
        return self._car_no

    @car_no.setter
    def car_no(self, value):
        self._car_no = value
    @property
    def driver_cert_no(self):
        return self._driver_cert_no

    @driver_cert_no.setter
    def driver_cert_no(self, value):
        self._driver_cert_no = value
    @property
    def driver_name(self):
        return self._driver_name

    @driver_name.setter
    def driver_name(self, value):
        self._driver_name = value
    @property
    def driver_sign_in_time(self):
        return self._driver_sign_in_time

    @driver_sign_in_time.setter
    def driver_sign_in_time(self, value):
        self._driver_sign_in_time = value
    @property
    def extra_amount(self):
        return self._extra_amount

    @extra_amount.setter
    def extra_amount(self, value):
        self._extra_amount = value
    @property
    def has_standby_driver(self):
        return self._has_standby_driver

    @has_standby_driver.setter
    def has_standby_driver(self, value):
        self._has_standby_driver = value
    @property
    def low_speed_wait_time(self):
        return self._low_speed_wait_time

    @low_speed_wait_time.setter
    def low_speed_wait_time(self, value):
        self._low_speed_wait_time = value
    @property
    def machine_sn(self):
        return self._machine_sn

    @machine_sn.setter
    def machine_sn(self, value):
        self._machine_sn = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def reserve(self):
        return self._reserve

    @reserve.setter
    def reserve(self, value):
        self._reserve = value
    @property
    def trip_amount(self):
        return self._trip_amount

    @trip_amount.setter
    def trip_amount(self, value):
        self._trip_amount = value
    @property
    def trip_cost_time(self):
        return self._trip_cost_time

    @trip_cost_time.setter
    def trip_cost_time(self, value):
        self._trip_cost_time = value
    @property
    def trip_end_location(self):
        return self._trip_end_location

    @trip_end_location.setter
    def trip_end_location(self, value):
        self._trip_end_location = value
    @property
    def trip_end_time(self):
        return self._trip_end_time

    @trip_end_time.setter
    def trip_end_time(self, value):
        self._trip_end_time = value
    @property
    def trip_id(self):
        return self._trip_id

    @trip_id.setter
    def trip_id(self, value):
        self._trip_id = value
    @property
    def trip_mileage(self):
        return self._trip_mileage

    @trip_mileage.setter
    def trip_mileage(self, value):
        self._trip_mileage = value
    @property
    def trip_start_location(self):
        return self._trip_start_location

    @trip_start_location.setter
    def trip_start_location(self, value):
        self._trip_start_location = value
    @property
    def trip_start_time(self):
        return self._trip_start_time

    @trip_start_time.setter
    def trip_start_time(self, value):
        self._trip_start_time = value
    @property
    def trip_type(self):
        return self._trip_type

    @trip_type.setter
    def trip_type(self, value):
        self._trip_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.car_no:
            if hasattr(self.car_no, 'to_alipay_dict'):
                params['car_no'] = self.car_no.to_alipay_dict()
            else:
                params['car_no'] = self.car_no
        if self.driver_cert_no:
            if hasattr(self.driver_cert_no, 'to_alipay_dict'):
                params['driver_cert_no'] = self.driver_cert_no.to_alipay_dict()
            else:
                params['driver_cert_no'] = self.driver_cert_no
        if self.driver_name:
            if hasattr(self.driver_name, 'to_alipay_dict'):
                params['driver_name'] = self.driver_name.to_alipay_dict()
            else:
                params['driver_name'] = self.driver_name
        if self.driver_sign_in_time:
            if hasattr(self.driver_sign_in_time, 'to_alipay_dict'):
                params['driver_sign_in_time'] = self.driver_sign_in_time.to_alipay_dict()
            else:
                params['driver_sign_in_time'] = self.driver_sign_in_time
        if self.extra_amount:
            if hasattr(self.extra_amount, 'to_alipay_dict'):
                params['extra_amount'] = self.extra_amount.to_alipay_dict()
            else:
                params['extra_amount'] = self.extra_amount
        if self.has_standby_driver:
            if hasattr(self.has_standby_driver, 'to_alipay_dict'):
                params['has_standby_driver'] = self.has_standby_driver.to_alipay_dict()
            else:
                params['has_standby_driver'] = self.has_standby_driver
        if self.low_speed_wait_time:
            if hasattr(self.low_speed_wait_time, 'to_alipay_dict'):
                params['low_speed_wait_time'] = self.low_speed_wait_time.to_alipay_dict()
            else:
                params['low_speed_wait_time'] = self.low_speed_wait_time
        if self.machine_sn:
            if hasattr(self.machine_sn, 'to_alipay_dict'):
                params['machine_sn'] = self.machine_sn.to_alipay_dict()
            else:
                params['machine_sn'] = self.machine_sn
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.reserve:
            if hasattr(self.reserve, 'to_alipay_dict'):
                params['reserve'] = self.reserve.to_alipay_dict()
            else:
                params['reserve'] = self.reserve
        if self.trip_amount:
            if hasattr(self.trip_amount, 'to_alipay_dict'):
                params['trip_amount'] = self.trip_amount.to_alipay_dict()
            else:
                params['trip_amount'] = self.trip_amount
        if self.trip_cost_time:
            if hasattr(self.trip_cost_time, 'to_alipay_dict'):
                params['trip_cost_time'] = self.trip_cost_time.to_alipay_dict()
            else:
                params['trip_cost_time'] = self.trip_cost_time
        if self.trip_end_location:
            if hasattr(self.trip_end_location, 'to_alipay_dict'):
                params['trip_end_location'] = self.trip_end_location.to_alipay_dict()
            else:
                params['trip_end_location'] = self.trip_end_location
        if self.trip_end_time:
            if hasattr(self.trip_end_time, 'to_alipay_dict'):
                params['trip_end_time'] = self.trip_end_time.to_alipay_dict()
            else:
                params['trip_end_time'] = self.trip_end_time
        if self.trip_id:
            if hasattr(self.trip_id, 'to_alipay_dict'):
                params['trip_id'] = self.trip_id.to_alipay_dict()
            else:
                params['trip_id'] = self.trip_id
        if self.trip_mileage:
            if hasattr(self.trip_mileage, 'to_alipay_dict'):
                params['trip_mileage'] = self.trip_mileage.to_alipay_dict()
            else:
                params['trip_mileage'] = self.trip_mileage
        if self.trip_start_location:
            if hasattr(self.trip_start_location, 'to_alipay_dict'):
                params['trip_start_location'] = self.trip_start_location.to_alipay_dict()
            else:
                params['trip_start_location'] = self.trip_start_location
        if self.trip_start_time:
            if hasattr(self.trip_start_time, 'to_alipay_dict'):
                params['trip_start_time'] = self.trip_start_time.to_alipay_dict()
            else:
                params['trip_start_time'] = self.trip_start_time
        if self.trip_type:
            if hasattr(self.trip_type, 'to_alipay_dict'):
                params['trip_type'] = self.trip_type.to_alipay_dict()
            else:
                params['trip_type'] = self.trip_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportTaxiTripUploadModel()
        if 'car_no' in d:
            o.car_no = d['car_no']
        if 'driver_cert_no' in d:
            o.driver_cert_no = d['driver_cert_no']
        if 'driver_name' in d:
            o.driver_name = d['driver_name']
        if 'driver_sign_in_time' in d:
            o.driver_sign_in_time = d['driver_sign_in_time']
        if 'extra_amount' in d:
            o.extra_amount = d['extra_amount']
        if 'has_standby_driver' in d:
            o.has_standby_driver = d['has_standby_driver']
        if 'low_speed_wait_time' in d:
            o.low_speed_wait_time = d['low_speed_wait_time']
        if 'machine_sn' in d:
            o.machine_sn = d['machine_sn']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'reserve' in d:
            o.reserve = d['reserve']
        if 'trip_amount' in d:
            o.trip_amount = d['trip_amount']
        if 'trip_cost_time' in d:
            o.trip_cost_time = d['trip_cost_time']
        if 'trip_end_location' in d:
            o.trip_end_location = d['trip_end_location']
        if 'trip_end_time' in d:
            o.trip_end_time = d['trip_end_time']
        if 'trip_id' in d:
            o.trip_id = d['trip_id']
        if 'trip_mileage' in d:
            o.trip_mileage = d['trip_mileage']
        if 'trip_start_location' in d:
            o.trip_start_location = d['trip_start_location']
        if 'trip_start_time' in d:
            o.trip_start_time = d['trip_start_time']
        if 'trip_type' in d:
            o.trip_type = d['trip_type']
        return o


