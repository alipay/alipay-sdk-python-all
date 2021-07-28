#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CarRentalInfo(object):

    def __init__(self):
        self._billing_start_time = None
        self._driving_duration = None
        self._driving_mileage = None
        self._duration_unit_price = None
        self._estimate_lease_end_time = None
        self._estimate_lease_start_time = None
        self._free_cancellation_time = None
        self._mileage_unit_price = None
        self._package_duration = None
        self._package_mileage = None
        self._package_name = None
        self._real_lease_end_time = None
        self._real_lease_start_time = None
        self._shopid_car_return = None
        self._shopid_car_taken = None
        self._upper_limit_amount = None

    @property
    def billing_start_time(self):
        return self._billing_start_time

    @billing_start_time.setter
    def billing_start_time(self, value):
        self._billing_start_time = value
    @property
    def driving_duration(self):
        return self._driving_duration

    @driving_duration.setter
    def driving_duration(self, value):
        self._driving_duration = value
    @property
    def driving_mileage(self):
        return self._driving_mileage

    @driving_mileage.setter
    def driving_mileage(self, value):
        self._driving_mileage = value
    @property
    def duration_unit_price(self):
        return self._duration_unit_price

    @duration_unit_price.setter
    def duration_unit_price(self, value):
        self._duration_unit_price = value
    @property
    def estimate_lease_end_time(self):
        return self._estimate_lease_end_time

    @estimate_lease_end_time.setter
    def estimate_lease_end_time(self, value):
        self._estimate_lease_end_time = value
    @property
    def estimate_lease_start_time(self):
        return self._estimate_lease_start_time

    @estimate_lease_start_time.setter
    def estimate_lease_start_time(self, value):
        self._estimate_lease_start_time = value
    @property
    def free_cancellation_time(self):
        return self._free_cancellation_time

    @free_cancellation_time.setter
    def free_cancellation_time(self, value):
        self._free_cancellation_time = value
    @property
    def mileage_unit_price(self):
        return self._mileage_unit_price

    @mileage_unit_price.setter
    def mileage_unit_price(self, value):
        self._mileage_unit_price = value
    @property
    def package_duration(self):
        return self._package_duration

    @package_duration.setter
    def package_duration(self, value):
        self._package_duration = value
    @property
    def package_mileage(self):
        return self._package_mileage

    @package_mileage.setter
    def package_mileage(self, value):
        self._package_mileage = value
    @property
    def package_name(self):
        return self._package_name

    @package_name.setter
    def package_name(self, value):
        self._package_name = value
    @property
    def real_lease_end_time(self):
        return self._real_lease_end_time

    @real_lease_end_time.setter
    def real_lease_end_time(self, value):
        self._real_lease_end_time = value
    @property
    def real_lease_start_time(self):
        return self._real_lease_start_time

    @real_lease_start_time.setter
    def real_lease_start_time(self, value):
        self._real_lease_start_time = value
    @property
    def shopid_car_return(self):
        return self._shopid_car_return

    @shopid_car_return.setter
    def shopid_car_return(self, value):
        self._shopid_car_return = value
    @property
    def shopid_car_taken(self):
        return self._shopid_car_taken

    @shopid_car_taken.setter
    def shopid_car_taken(self, value):
        self._shopid_car_taken = value
    @property
    def upper_limit_amount(self):
        return self._upper_limit_amount

    @upper_limit_amount.setter
    def upper_limit_amount(self, value):
        self._upper_limit_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.billing_start_time:
            if hasattr(self.billing_start_time, 'to_alipay_dict'):
                params['billing_start_time'] = self.billing_start_time.to_alipay_dict()
            else:
                params['billing_start_time'] = self.billing_start_time
        if self.driving_duration:
            if hasattr(self.driving_duration, 'to_alipay_dict'):
                params['driving_duration'] = self.driving_duration.to_alipay_dict()
            else:
                params['driving_duration'] = self.driving_duration
        if self.driving_mileage:
            if hasattr(self.driving_mileage, 'to_alipay_dict'):
                params['driving_mileage'] = self.driving_mileage.to_alipay_dict()
            else:
                params['driving_mileage'] = self.driving_mileage
        if self.duration_unit_price:
            if hasattr(self.duration_unit_price, 'to_alipay_dict'):
                params['duration_unit_price'] = self.duration_unit_price.to_alipay_dict()
            else:
                params['duration_unit_price'] = self.duration_unit_price
        if self.estimate_lease_end_time:
            if hasattr(self.estimate_lease_end_time, 'to_alipay_dict'):
                params['estimate_lease_end_time'] = self.estimate_lease_end_time.to_alipay_dict()
            else:
                params['estimate_lease_end_time'] = self.estimate_lease_end_time
        if self.estimate_lease_start_time:
            if hasattr(self.estimate_lease_start_time, 'to_alipay_dict'):
                params['estimate_lease_start_time'] = self.estimate_lease_start_time.to_alipay_dict()
            else:
                params['estimate_lease_start_time'] = self.estimate_lease_start_time
        if self.free_cancellation_time:
            if hasattr(self.free_cancellation_time, 'to_alipay_dict'):
                params['free_cancellation_time'] = self.free_cancellation_time.to_alipay_dict()
            else:
                params['free_cancellation_time'] = self.free_cancellation_time
        if self.mileage_unit_price:
            if hasattr(self.mileage_unit_price, 'to_alipay_dict'):
                params['mileage_unit_price'] = self.mileage_unit_price.to_alipay_dict()
            else:
                params['mileage_unit_price'] = self.mileage_unit_price
        if self.package_duration:
            if hasattr(self.package_duration, 'to_alipay_dict'):
                params['package_duration'] = self.package_duration.to_alipay_dict()
            else:
                params['package_duration'] = self.package_duration
        if self.package_mileage:
            if hasattr(self.package_mileage, 'to_alipay_dict'):
                params['package_mileage'] = self.package_mileage.to_alipay_dict()
            else:
                params['package_mileage'] = self.package_mileage
        if self.package_name:
            if hasattr(self.package_name, 'to_alipay_dict'):
                params['package_name'] = self.package_name.to_alipay_dict()
            else:
                params['package_name'] = self.package_name
        if self.real_lease_end_time:
            if hasattr(self.real_lease_end_time, 'to_alipay_dict'):
                params['real_lease_end_time'] = self.real_lease_end_time.to_alipay_dict()
            else:
                params['real_lease_end_time'] = self.real_lease_end_time
        if self.real_lease_start_time:
            if hasattr(self.real_lease_start_time, 'to_alipay_dict'):
                params['real_lease_start_time'] = self.real_lease_start_time.to_alipay_dict()
            else:
                params['real_lease_start_time'] = self.real_lease_start_time
        if self.shopid_car_return:
            if hasattr(self.shopid_car_return, 'to_alipay_dict'):
                params['shopid_car_return'] = self.shopid_car_return.to_alipay_dict()
            else:
                params['shopid_car_return'] = self.shopid_car_return
        if self.shopid_car_taken:
            if hasattr(self.shopid_car_taken, 'to_alipay_dict'):
                params['shopid_car_taken'] = self.shopid_car_taken.to_alipay_dict()
            else:
                params['shopid_car_taken'] = self.shopid_car_taken
        if self.upper_limit_amount:
            if hasattr(self.upper_limit_amount, 'to_alipay_dict'):
                params['upper_limit_amount'] = self.upper_limit_amount.to_alipay_dict()
            else:
                params['upper_limit_amount'] = self.upper_limit_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CarRentalInfo()
        if 'billing_start_time' in d:
            o.billing_start_time = d['billing_start_time']
        if 'driving_duration' in d:
            o.driving_duration = d['driving_duration']
        if 'driving_mileage' in d:
            o.driving_mileage = d['driving_mileage']
        if 'duration_unit_price' in d:
            o.duration_unit_price = d['duration_unit_price']
        if 'estimate_lease_end_time' in d:
            o.estimate_lease_end_time = d['estimate_lease_end_time']
        if 'estimate_lease_start_time' in d:
            o.estimate_lease_start_time = d['estimate_lease_start_time']
        if 'free_cancellation_time' in d:
            o.free_cancellation_time = d['free_cancellation_time']
        if 'mileage_unit_price' in d:
            o.mileage_unit_price = d['mileage_unit_price']
        if 'package_duration' in d:
            o.package_duration = d['package_duration']
        if 'package_mileage' in d:
            o.package_mileage = d['package_mileage']
        if 'package_name' in d:
            o.package_name = d['package_name']
        if 'real_lease_end_time' in d:
            o.real_lease_end_time = d['real_lease_end_time']
        if 'real_lease_start_time' in d:
            o.real_lease_start_time = d['real_lease_start_time']
        if 'shopid_car_return' in d:
            o.shopid_car_return = d['shopid_car_return']
        if 'shopid_car_taken' in d:
            o.shopid_car_taken = d['shopid_car_taken']
        if 'upper_limit_amount' in d:
            o.upper_limit_amount = d['upper_limit_amount']
        return o


