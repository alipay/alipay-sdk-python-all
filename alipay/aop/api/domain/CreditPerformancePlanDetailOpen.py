#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreditPerformancePlanDetailOpen(object):

    def __init__(self):
        self._actual_amount = None
        self._expected_pay_time = None
        self._plan_detail_number = None

    @property
    def actual_amount(self):
        return self._actual_amount

    @actual_amount.setter
    def actual_amount(self, value):
        self._actual_amount = value
    @property
    def expected_pay_time(self):
        return self._expected_pay_time

    @expected_pay_time.setter
    def expected_pay_time(self, value):
        self._expected_pay_time = value
    @property
    def plan_detail_number(self):
        return self._plan_detail_number

    @plan_detail_number.setter
    def plan_detail_number(self, value):
        self._plan_detail_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_amount:
            if hasattr(self.actual_amount, 'to_alipay_dict'):
                params['actual_amount'] = self.actual_amount.to_alipay_dict()
            else:
                params['actual_amount'] = self.actual_amount
        if self.expected_pay_time:
            if hasattr(self.expected_pay_time, 'to_alipay_dict'):
                params['expected_pay_time'] = self.expected_pay_time.to_alipay_dict()
            else:
                params['expected_pay_time'] = self.expected_pay_time
        if self.plan_detail_number:
            if hasattr(self.plan_detail_number, 'to_alipay_dict'):
                params['plan_detail_number'] = self.plan_detail_number.to_alipay_dict()
            else:
                params['plan_detail_number'] = self.plan_detail_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditPerformancePlanDetailOpen()
        if 'actual_amount' in d:
            o.actual_amount = d['actual_amount']
        if 'expected_pay_time' in d:
            o.expected_pay_time = d['expected_pay_time']
        if 'plan_detail_number' in d:
            o.plan_detail_number = d['plan_detail_number']
        return o


