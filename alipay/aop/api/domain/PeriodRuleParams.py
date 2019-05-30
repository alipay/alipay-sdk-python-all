#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PeriodRuleParams(object):

    def __init__(self):
        self._execute_time = None
        self._period = None
        self._period_type = None
        self._single_amount = None
        self._total_amount = None
        self._total_payments = None

    @property
    def execute_time(self):
        return self._execute_time

    @execute_time.setter
    def execute_time(self, value):
        self._execute_time = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def period_type(self):
        return self._period_type

    @period_type.setter
    def period_type(self, value):
        self._period_type = value
    @property
    def single_amount(self):
        return self._single_amount

    @single_amount.setter
    def single_amount(self, value):
        self._single_amount = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def total_payments(self):
        return self._total_payments

    @total_payments.setter
    def total_payments(self, value):
        self._total_payments = value


    def to_alipay_dict(self):
        params = dict()
        if self.execute_time:
            if hasattr(self.execute_time, 'to_alipay_dict'):
                params['execute_time'] = self.execute_time.to_alipay_dict()
            else:
                params['execute_time'] = self.execute_time
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.period_type:
            if hasattr(self.period_type, 'to_alipay_dict'):
                params['period_type'] = self.period_type.to_alipay_dict()
            else:
                params['period_type'] = self.period_type
        if self.single_amount:
            if hasattr(self.single_amount, 'to_alipay_dict'):
                params['single_amount'] = self.single_amount.to_alipay_dict()
            else:
                params['single_amount'] = self.single_amount
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.total_payments:
            if hasattr(self.total_payments, 'to_alipay_dict'):
                params['total_payments'] = self.total_payments.to_alipay_dict()
            else:
                params['total_payments'] = self.total_payments
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PeriodRuleParams()
        if 'execute_time' in d:
            o.execute_time = d['execute_time']
        if 'period' in d:
            o.period = d['period']
        if 'period_type' in d:
            o.period_type = d['period_type']
        if 'single_amount' in d:
            o.single_amount = d['single_amount']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'total_payments' in d:
            o.total_payments = d['total_payments']
        return o


