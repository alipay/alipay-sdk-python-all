#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CarSubscriptionOrder(object):

    def __init__(self):
        self._car_deposit = None
        self._insurance_premium = None
        self._large_deposit_amount = None
        self._rental_fee_per_period = None
        self._rental_fee_per_period_of_basic = None
        self._rental_fee_per_period_of_insurance = None
        self._rental_fee_per_period_of_mileage = None
        self._rental_fee_per_period_of_quota = None
        self._small_deposit_amount = None
        self._subscription_duration = None
        self._subscription_duration_unit = None
        self._subscription_mileage = None
        self._traffic_violation_deposit = None

    @property
    def car_deposit(self):
        return self._car_deposit

    @car_deposit.setter
    def car_deposit(self, value):
        self._car_deposit = value
    @property
    def insurance_premium(self):
        return self._insurance_premium

    @insurance_premium.setter
    def insurance_premium(self, value):
        self._insurance_premium = value
    @property
    def large_deposit_amount(self):
        return self._large_deposit_amount

    @large_deposit_amount.setter
    def large_deposit_amount(self, value):
        self._large_deposit_amount = value
    @property
    def rental_fee_per_period(self):
        return self._rental_fee_per_period

    @rental_fee_per_period.setter
    def rental_fee_per_period(self, value):
        self._rental_fee_per_period = value
    @property
    def rental_fee_per_period_of_basic(self):
        return self._rental_fee_per_period_of_basic

    @rental_fee_per_period_of_basic.setter
    def rental_fee_per_period_of_basic(self, value):
        self._rental_fee_per_period_of_basic = value
    @property
    def rental_fee_per_period_of_insurance(self):
        return self._rental_fee_per_period_of_insurance

    @rental_fee_per_period_of_insurance.setter
    def rental_fee_per_period_of_insurance(self, value):
        self._rental_fee_per_period_of_insurance = value
    @property
    def rental_fee_per_period_of_mileage(self):
        return self._rental_fee_per_period_of_mileage

    @rental_fee_per_period_of_mileage.setter
    def rental_fee_per_period_of_mileage(self, value):
        self._rental_fee_per_period_of_mileage = value
    @property
    def rental_fee_per_period_of_quota(self):
        return self._rental_fee_per_period_of_quota

    @rental_fee_per_period_of_quota.setter
    def rental_fee_per_period_of_quota(self, value):
        self._rental_fee_per_period_of_quota = value
    @property
    def small_deposit_amount(self):
        return self._small_deposit_amount

    @small_deposit_amount.setter
    def small_deposit_amount(self, value):
        self._small_deposit_amount = value
    @property
    def subscription_duration(self):
        return self._subscription_duration

    @subscription_duration.setter
    def subscription_duration(self, value):
        self._subscription_duration = value
    @property
    def subscription_duration_unit(self):
        return self._subscription_duration_unit

    @subscription_duration_unit.setter
    def subscription_duration_unit(self, value):
        self._subscription_duration_unit = value
    @property
    def subscription_mileage(self):
        return self._subscription_mileage

    @subscription_mileage.setter
    def subscription_mileage(self, value):
        self._subscription_mileage = value
    @property
    def traffic_violation_deposit(self):
        return self._traffic_violation_deposit

    @traffic_violation_deposit.setter
    def traffic_violation_deposit(self, value):
        self._traffic_violation_deposit = value


    def to_alipay_dict(self):
        params = dict()
        if self.car_deposit:
            if hasattr(self.car_deposit, 'to_alipay_dict'):
                params['car_deposit'] = self.car_deposit.to_alipay_dict()
            else:
                params['car_deposit'] = self.car_deposit
        if self.insurance_premium:
            if hasattr(self.insurance_premium, 'to_alipay_dict'):
                params['insurance_premium'] = self.insurance_premium.to_alipay_dict()
            else:
                params['insurance_premium'] = self.insurance_premium
        if self.large_deposit_amount:
            if hasattr(self.large_deposit_amount, 'to_alipay_dict'):
                params['large_deposit_amount'] = self.large_deposit_amount.to_alipay_dict()
            else:
                params['large_deposit_amount'] = self.large_deposit_amount
        if self.rental_fee_per_period:
            if hasattr(self.rental_fee_per_period, 'to_alipay_dict'):
                params['rental_fee_per_period'] = self.rental_fee_per_period.to_alipay_dict()
            else:
                params['rental_fee_per_period'] = self.rental_fee_per_period
        if self.rental_fee_per_period_of_basic:
            if hasattr(self.rental_fee_per_period_of_basic, 'to_alipay_dict'):
                params['rental_fee_per_period_of_basic'] = self.rental_fee_per_period_of_basic.to_alipay_dict()
            else:
                params['rental_fee_per_period_of_basic'] = self.rental_fee_per_period_of_basic
        if self.rental_fee_per_period_of_insurance:
            if hasattr(self.rental_fee_per_period_of_insurance, 'to_alipay_dict'):
                params['rental_fee_per_period_of_insurance'] = self.rental_fee_per_period_of_insurance.to_alipay_dict()
            else:
                params['rental_fee_per_period_of_insurance'] = self.rental_fee_per_period_of_insurance
        if self.rental_fee_per_period_of_mileage:
            if hasattr(self.rental_fee_per_period_of_mileage, 'to_alipay_dict'):
                params['rental_fee_per_period_of_mileage'] = self.rental_fee_per_period_of_mileage.to_alipay_dict()
            else:
                params['rental_fee_per_period_of_mileage'] = self.rental_fee_per_period_of_mileage
        if self.rental_fee_per_period_of_quota:
            if hasattr(self.rental_fee_per_period_of_quota, 'to_alipay_dict'):
                params['rental_fee_per_period_of_quota'] = self.rental_fee_per_period_of_quota.to_alipay_dict()
            else:
                params['rental_fee_per_period_of_quota'] = self.rental_fee_per_period_of_quota
        if self.small_deposit_amount:
            if hasattr(self.small_deposit_amount, 'to_alipay_dict'):
                params['small_deposit_amount'] = self.small_deposit_amount.to_alipay_dict()
            else:
                params['small_deposit_amount'] = self.small_deposit_amount
        if self.subscription_duration:
            if hasattr(self.subscription_duration, 'to_alipay_dict'):
                params['subscription_duration'] = self.subscription_duration.to_alipay_dict()
            else:
                params['subscription_duration'] = self.subscription_duration
        if self.subscription_duration_unit:
            if hasattr(self.subscription_duration_unit, 'to_alipay_dict'):
                params['subscription_duration_unit'] = self.subscription_duration_unit.to_alipay_dict()
            else:
                params['subscription_duration_unit'] = self.subscription_duration_unit
        if self.subscription_mileage:
            if hasattr(self.subscription_mileage, 'to_alipay_dict'):
                params['subscription_mileage'] = self.subscription_mileage.to_alipay_dict()
            else:
                params['subscription_mileage'] = self.subscription_mileage
        if self.traffic_violation_deposit:
            if hasattr(self.traffic_violation_deposit, 'to_alipay_dict'):
                params['traffic_violation_deposit'] = self.traffic_violation_deposit.to_alipay_dict()
            else:
                params['traffic_violation_deposit'] = self.traffic_violation_deposit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CarSubscriptionOrder()
        if 'car_deposit' in d:
            o.car_deposit = d['car_deposit']
        if 'insurance_premium' in d:
            o.insurance_premium = d['insurance_premium']
        if 'large_deposit_amount' in d:
            o.large_deposit_amount = d['large_deposit_amount']
        if 'rental_fee_per_period' in d:
            o.rental_fee_per_period = d['rental_fee_per_period']
        if 'rental_fee_per_period_of_basic' in d:
            o.rental_fee_per_period_of_basic = d['rental_fee_per_period_of_basic']
        if 'rental_fee_per_period_of_insurance' in d:
            o.rental_fee_per_period_of_insurance = d['rental_fee_per_period_of_insurance']
        if 'rental_fee_per_period_of_mileage' in d:
            o.rental_fee_per_period_of_mileage = d['rental_fee_per_period_of_mileage']
        if 'rental_fee_per_period_of_quota' in d:
            o.rental_fee_per_period_of_quota = d['rental_fee_per_period_of_quota']
        if 'small_deposit_amount' in d:
            o.small_deposit_amount = d['small_deposit_amount']
        if 'subscription_duration' in d:
            o.subscription_duration = d['subscription_duration']
        if 'subscription_duration_unit' in d:
            o.subscription_duration_unit = d['subscription_duration_unit']
        if 'subscription_mileage' in d:
            o.subscription_mileage = d['subscription_mileage']
        if 'traffic_violation_deposit' in d:
            o.traffic_violation_deposit = d['traffic_violation_deposit']
        return o


