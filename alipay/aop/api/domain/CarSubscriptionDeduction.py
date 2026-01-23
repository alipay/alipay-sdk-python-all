#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CarSubscriptionDeduction(object):

    def __init__(self):
        self._car_deposit_deduct_amount = None
        self._rental_fee_commission = None
        self._rental_fee_deduct_amount = None
        self._rental_fee_deduct_amount_of_basic = None
        self._rental_fee_deduct_amount_of_insurance = None
        self._rental_fee_deduct_amount_of_mileage = None
        self._rental_fee_deduct_amount_of_quota = None
        self._rental_fee_deduct_round = None
        self._rental_fee_deduct_status = None
        self._rental_fee_deduct_time = None
        self._traffic_violation_deposit_deduct_amount = None

    @property
    def car_deposit_deduct_amount(self):
        return self._car_deposit_deduct_amount

    @car_deposit_deduct_amount.setter
    def car_deposit_deduct_amount(self, value):
        self._car_deposit_deduct_amount = value
    @property
    def rental_fee_commission(self):
        return self._rental_fee_commission

    @rental_fee_commission.setter
    def rental_fee_commission(self, value):
        self._rental_fee_commission = value
    @property
    def rental_fee_deduct_amount(self):
        return self._rental_fee_deduct_amount

    @rental_fee_deduct_amount.setter
    def rental_fee_deduct_amount(self, value):
        self._rental_fee_deduct_amount = value
    @property
    def rental_fee_deduct_amount_of_basic(self):
        return self._rental_fee_deduct_amount_of_basic

    @rental_fee_deduct_amount_of_basic.setter
    def rental_fee_deduct_amount_of_basic(self, value):
        self._rental_fee_deduct_amount_of_basic = value
    @property
    def rental_fee_deduct_amount_of_insurance(self):
        return self._rental_fee_deduct_amount_of_insurance

    @rental_fee_deduct_amount_of_insurance.setter
    def rental_fee_deduct_amount_of_insurance(self, value):
        self._rental_fee_deduct_amount_of_insurance = value
    @property
    def rental_fee_deduct_amount_of_mileage(self):
        return self._rental_fee_deduct_amount_of_mileage

    @rental_fee_deduct_amount_of_mileage.setter
    def rental_fee_deduct_amount_of_mileage(self, value):
        self._rental_fee_deduct_amount_of_mileage = value
    @property
    def rental_fee_deduct_amount_of_quota(self):
        return self._rental_fee_deduct_amount_of_quota

    @rental_fee_deduct_amount_of_quota.setter
    def rental_fee_deduct_amount_of_quota(self, value):
        self._rental_fee_deduct_amount_of_quota = value
    @property
    def rental_fee_deduct_round(self):
        return self._rental_fee_deduct_round

    @rental_fee_deduct_round.setter
    def rental_fee_deduct_round(self, value):
        self._rental_fee_deduct_round = value
    @property
    def rental_fee_deduct_status(self):
        return self._rental_fee_deduct_status

    @rental_fee_deduct_status.setter
    def rental_fee_deduct_status(self, value):
        self._rental_fee_deduct_status = value
    @property
    def rental_fee_deduct_time(self):
        return self._rental_fee_deduct_time

    @rental_fee_deduct_time.setter
    def rental_fee_deduct_time(self, value):
        self._rental_fee_deduct_time = value
    @property
    def traffic_violation_deposit_deduct_amount(self):
        return self._traffic_violation_deposit_deduct_amount

    @traffic_violation_deposit_deduct_amount.setter
    def traffic_violation_deposit_deduct_amount(self, value):
        self._traffic_violation_deposit_deduct_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.car_deposit_deduct_amount:
            if hasattr(self.car_deposit_deduct_amount, 'to_alipay_dict'):
                params['car_deposit_deduct_amount'] = self.car_deposit_deduct_amount.to_alipay_dict()
            else:
                params['car_deposit_deduct_amount'] = self.car_deposit_deduct_amount
        if self.rental_fee_commission:
            if hasattr(self.rental_fee_commission, 'to_alipay_dict'):
                params['rental_fee_commission'] = self.rental_fee_commission.to_alipay_dict()
            else:
                params['rental_fee_commission'] = self.rental_fee_commission
        if self.rental_fee_deduct_amount:
            if hasattr(self.rental_fee_deduct_amount, 'to_alipay_dict'):
                params['rental_fee_deduct_amount'] = self.rental_fee_deduct_amount.to_alipay_dict()
            else:
                params['rental_fee_deduct_amount'] = self.rental_fee_deduct_amount
        if self.rental_fee_deduct_amount_of_basic:
            if hasattr(self.rental_fee_deduct_amount_of_basic, 'to_alipay_dict'):
                params['rental_fee_deduct_amount_of_basic'] = self.rental_fee_deduct_amount_of_basic.to_alipay_dict()
            else:
                params['rental_fee_deduct_amount_of_basic'] = self.rental_fee_deduct_amount_of_basic
        if self.rental_fee_deduct_amount_of_insurance:
            if hasattr(self.rental_fee_deduct_amount_of_insurance, 'to_alipay_dict'):
                params['rental_fee_deduct_amount_of_insurance'] = self.rental_fee_deduct_amount_of_insurance.to_alipay_dict()
            else:
                params['rental_fee_deduct_amount_of_insurance'] = self.rental_fee_deduct_amount_of_insurance
        if self.rental_fee_deduct_amount_of_mileage:
            if hasattr(self.rental_fee_deduct_amount_of_mileage, 'to_alipay_dict'):
                params['rental_fee_deduct_amount_of_mileage'] = self.rental_fee_deduct_amount_of_mileage.to_alipay_dict()
            else:
                params['rental_fee_deduct_amount_of_mileage'] = self.rental_fee_deduct_amount_of_mileage
        if self.rental_fee_deduct_amount_of_quota:
            if hasattr(self.rental_fee_deduct_amount_of_quota, 'to_alipay_dict'):
                params['rental_fee_deduct_amount_of_quota'] = self.rental_fee_deduct_amount_of_quota.to_alipay_dict()
            else:
                params['rental_fee_deduct_amount_of_quota'] = self.rental_fee_deduct_amount_of_quota
        if self.rental_fee_deduct_round:
            if hasattr(self.rental_fee_deduct_round, 'to_alipay_dict'):
                params['rental_fee_deduct_round'] = self.rental_fee_deduct_round.to_alipay_dict()
            else:
                params['rental_fee_deduct_round'] = self.rental_fee_deduct_round
        if self.rental_fee_deduct_status:
            if hasattr(self.rental_fee_deduct_status, 'to_alipay_dict'):
                params['rental_fee_deduct_status'] = self.rental_fee_deduct_status.to_alipay_dict()
            else:
                params['rental_fee_deduct_status'] = self.rental_fee_deduct_status
        if self.rental_fee_deduct_time:
            if hasattr(self.rental_fee_deduct_time, 'to_alipay_dict'):
                params['rental_fee_deduct_time'] = self.rental_fee_deduct_time.to_alipay_dict()
            else:
                params['rental_fee_deduct_time'] = self.rental_fee_deduct_time
        if self.traffic_violation_deposit_deduct_amount:
            if hasattr(self.traffic_violation_deposit_deduct_amount, 'to_alipay_dict'):
                params['traffic_violation_deposit_deduct_amount'] = self.traffic_violation_deposit_deduct_amount.to_alipay_dict()
            else:
                params['traffic_violation_deposit_deduct_amount'] = self.traffic_violation_deposit_deduct_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CarSubscriptionDeduction()
        if 'car_deposit_deduct_amount' in d:
            o.car_deposit_deduct_amount = d['car_deposit_deduct_amount']
        if 'rental_fee_commission' in d:
            o.rental_fee_commission = d['rental_fee_commission']
        if 'rental_fee_deduct_amount' in d:
            o.rental_fee_deduct_amount = d['rental_fee_deduct_amount']
        if 'rental_fee_deduct_amount_of_basic' in d:
            o.rental_fee_deduct_amount_of_basic = d['rental_fee_deduct_amount_of_basic']
        if 'rental_fee_deduct_amount_of_insurance' in d:
            o.rental_fee_deduct_amount_of_insurance = d['rental_fee_deduct_amount_of_insurance']
        if 'rental_fee_deduct_amount_of_mileage' in d:
            o.rental_fee_deduct_amount_of_mileage = d['rental_fee_deduct_amount_of_mileage']
        if 'rental_fee_deduct_amount_of_quota' in d:
            o.rental_fee_deduct_amount_of_quota = d['rental_fee_deduct_amount_of_quota']
        if 'rental_fee_deduct_round' in d:
            o.rental_fee_deduct_round = d['rental_fee_deduct_round']
        if 'rental_fee_deduct_status' in d:
            o.rental_fee_deduct_status = d['rental_fee_deduct_status']
        if 'rental_fee_deduct_time' in d:
            o.rental_fee_deduct_time = d['rental_fee_deduct_time']
        if 'traffic_violation_deposit_deduct_amount' in d:
            o.traffic_violation_deposit_deduct_amount = d['traffic_violation_deposit_deduct_amount']
        return o


