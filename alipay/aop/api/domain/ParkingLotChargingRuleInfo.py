#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ParkingLotChargingRuleInfo(object):

    def __init__(self):
        self._charging_period = None
        self._charging_strategy = None
        self._charging_unit_fee = None
        self._charging_unit_minutes = None
        self._enable_rollover_charge_period = None
        self._first_charging_span_minutes = None
        self._first_charging_unit_fee = None
        self._first_charging_unit_minutes = None
        self._free_enter_minutes = None
        self._free_exit_minutes = None
        self._max_fee_per_day = None

    @property
    def charging_period(self):
        return self._charging_period

    @charging_period.setter
    def charging_period(self, value):
        self._charging_period = value
    @property
    def charging_strategy(self):
        return self._charging_strategy

    @charging_strategy.setter
    def charging_strategy(self, value):
        self._charging_strategy = value
    @property
    def charging_unit_fee(self):
        return self._charging_unit_fee

    @charging_unit_fee.setter
    def charging_unit_fee(self, value):
        self._charging_unit_fee = value
    @property
    def charging_unit_minutes(self):
        return self._charging_unit_minutes

    @charging_unit_minutes.setter
    def charging_unit_minutes(self, value):
        self._charging_unit_minutes = value
    @property
    def enable_rollover_charge_period(self):
        return self._enable_rollover_charge_period

    @enable_rollover_charge_period.setter
    def enable_rollover_charge_period(self, value):
        self._enable_rollover_charge_period = value
    @property
    def first_charging_span_minutes(self):
        return self._first_charging_span_minutes

    @first_charging_span_minutes.setter
    def first_charging_span_minutes(self, value):
        self._first_charging_span_minutes = value
    @property
    def first_charging_unit_fee(self):
        return self._first_charging_unit_fee

    @first_charging_unit_fee.setter
    def first_charging_unit_fee(self, value):
        self._first_charging_unit_fee = value
    @property
    def first_charging_unit_minutes(self):
        return self._first_charging_unit_minutes

    @first_charging_unit_minutes.setter
    def first_charging_unit_minutes(self, value):
        self._first_charging_unit_minutes = value
    @property
    def free_enter_minutes(self):
        return self._free_enter_minutes

    @free_enter_minutes.setter
    def free_enter_minutes(self, value):
        self._free_enter_minutes = value
    @property
    def free_exit_minutes(self):
        return self._free_exit_minutes

    @free_exit_minutes.setter
    def free_exit_minutes(self, value):
        self._free_exit_minutes = value
    @property
    def max_fee_per_day(self):
        return self._max_fee_per_day

    @max_fee_per_day.setter
    def max_fee_per_day(self, value):
        self._max_fee_per_day = value


    def to_alipay_dict(self):
        params = dict()
        if self.charging_period:
            if hasattr(self.charging_period, 'to_alipay_dict'):
                params['charging_period'] = self.charging_period.to_alipay_dict()
            else:
                params['charging_period'] = self.charging_period
        if self.charging_strategy:
            if hasattr(self.charging_strategy, 'to_alipay_dict'):
                params['charging_strategy'] = self.charging_strategy.to_alipay_dict()
            else:
                params['charging_strategy'] = self.charging_strategy
        if self.charging_unit_fee:
            if hasattr(self.charging_unit_fee, 'to_alipay_dict'):
                params['charging_unit_fee'] = self.charging_unit_fee.to_alipay_dict()
            else:
                params['charging_unit_fee'] = self.charging_unit_fee
        if self.charging_unit_minutes:
            if hasattr(self.charging_unit_minutes, 'to_alipay_dict'):
                params['charging_unit_minutes'] = self.charging_unit_minutes.to_alipay_dict()
            else:
                params['charging_unit_minutes'] = self.charging_unit_minutes
        if self.enable_rollover_charge_period:
            if hasattr(self.enable_rollover_charge_period, 'to_alipay_dict'):
                params['enable_rollover_charge_period'] = self.enable_rollover_charge_period.to_alipay_dict()
            else:
                params['enable_rollover_charge_period'] = self.enable_rollover_charge_period
        if self.first_charging_span_minutes:
            if hasattr(self.first_charging_span_minutes, 'to_alipay_dict'):
                params['first_charging_span_minutes'] = self.first_charging_span_minutes.to_alipay_dict()
            else:
                params['first_charging_span_minutes'] = self.first_charging_span_minutes
        if self.first_charging_unit_fee:
            if hasattr(self.first_charging_unit_fee, 'to_alipay_dict'):
                params['first_charging_unit_fee'] = self.first_charging_unit_fee.to_alipay_dict()
            else:
                params['first_charging_unit_fee'] = self.first_charging_unit_fee
        if self.first_charging_unit_minutes:
            if hasattr(self.first_charging_unit_minutes, 'to_alipay_dict'):
                params['first_charging_unit_minutes'] = self.first_charging_unit_minutes.to_alipay_dict()
            else:
                params['first_charging_unit_minutes'] = self.first_charging_unit_minutes
        if self.free_enter_minutes:
            if hasattr(self.free_enter_minutes, 'to_alipay_dict'):
                params['free_enter_minutes'] = self.free_enter_minutes.to_alipay_dict()
            else:
                params['free_enter_minutes'] = self.free_enter_minutes
        if self.free_exit_minutes:
            if hasattr(self.free_exit_minutes, 'to_alipay_dict'):
                params['free_exit_minutes'] = self.free_exit_minutes.to_alipay_dict()
            else:
                params['free_exit_minutes'] = self.free_exit_minutes
        if self.max_fee_per_day:
            if hasattr(self.max_fee_per_day, 'to_alipay_dict'):
                params['max_fee_per_day'] = self.max_fee_per_day.to_alipay_dict()
            else:
                params['max_fee_per_day'] = self.max_fee_per_day
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ParkingLotChargingRuleInfo()
        if 'charging_period' in d:
            o.charging_period = d['charging_period']
        if 'charging_strategy' in d:
            o.charging_strategy = d['charging_strategy']
        if 'charging_unit_fee' in d:
            o.charging_unit_fee = d['charging_unit_fee']
        if 'charging_unit_minutes' in d:
            o.charging_unit_minutes = d['charging_unit_minutes']
        if 'enable_rollover_charge_period' in d:
            o.enable_rollover_charge_period = d['enable_rollover_charge_period']
        if 'first_charging_span_minutes' in d:
            o.first_charging_span_minutes = d['first_charging_span_minutes']
        if 'first_charging_unit_fee' in d:
            o.first_charging_unit_fee = d['first_charging_unit_fee']
        if 'first_charging_unit_minutes' in d:
            o.first_charging_unit_minutes = d['first_charging_unit_minutes']
        if 'free_enter_minutes' in d:
            o.free_enter_minutes = d['free_enter_minutes']
        if 'free_exit_minutes' in d:
            o.free_exit_minutes = d['free_exit_minutes']
        if 'max_fee_per_day' in d:
            o.max_fee_per_day = d['max_fee_per_day']
        return o


