#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreditPerformancePlanDetailOpen import CreditPerformancePlanDetailOpen


class CreditPerformancePlanInfoOpen(object):

    def __init__(self):
        self._plan_details = None
        self._times = None
        self._total_actual_amount = None

    @property
    def plan_details(self):
        return self._plan_details

    @plan_details.setter
    def plan_details(self, value):
        if isinstance(value, list):
            self._plan_details = list()
            for i in value:
                if isinstance(i, CreditPerformancePlanDetailOpen):
                    self._plan_details.append(i)
                else:
                    self._plan_details.append(CreditPerformancePlanDetailOpen.from_alipay_dict(i))
    @property
    def times(self):
        return self._times

    @times.setter
    def times(self, value):
        self._times = value
    @property
    def total_actual_amount(self):
        return self._total_actual_amount

    @total_actual_amount.setter
    def total_actual_amount(self, value):
        self._total_actual_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.plan_details:
            if isinstance(self.plan_details, list):
                for i in range(0, len(self.plan_details)):
                    element = self.plan_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.plan_details[i] = element.to_alipay_dict()
            if hasattr(self.plan_details, 'to_alipay_dict'):
                params['plan_details'] = self.plan_details.to_alipay_dict()
            else:
                params['plan_details'] = self.plan_details
        if self.times:
            if hasattr(self.times, 'to_alipay_dict'):
                params['times'] = self.times.to_alipay_dict()
            else:
                params['times'] = self.times
        if self.total_actual_amount:
            if hasattr(self.total_actual_amount, 'to_alipay_dict'):
                params['total_actual_amount'] = self.total_actual_amount.to_alipay_dict()
            else:
                params['total_actual_amount'] = self.total_actual_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditPerformancePlanInfoOpen()
        if 'plan_details' in d:
            o.plan_details = d['plan_details']
        if 'times' in d:
            o.times = d['times']
        if 'total_actual_amount' in d:
            o.total_actual_amount = d['total_actual_amount']
        return o


