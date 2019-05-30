#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ActivityRuleDetail(object):

    def __init__(self):
        self._rule_amount = None
        self._rule_discount = None
        self._rule_period = None
        self._rule_period_unit = None
        self._rule_times = None

    @property
    def rule_amount(self):
        return self._rule_amount

    @rule_amount.setter
    def rule_amount(self, value):
        self._rule_amount = value
    @property
    def rule_discount(self):
        return self._rule_discount

    @rule_discount.setter
    def rule_discount(self, value):
        self._rule_discount = value
    @property
    def rule_period(self):
        return self._rule_period

    @rule_period.setter
    def rule_period(self, value):
        self._rule_period = value
    @property
    def rule_period_unit(self):
        return self._rule_period_unit

    @rule_period_unit.setter
    def rule_period_unit(self, value):
        self._rule_period_unit = value
    @property
    def rule_times(self):
        return self._rule_times

    @rule_times.setter
    def rule_times(self, value):
        self._rule_times = value


    def to_alipay_dict(self):
        params = dict()
        if self.rule_amount:
            if hasattr(self.rule_amount, 'to_alipay_dict'):
                params['rule_amount'] = self.rule_amount.to_alipay_dict()
            else:
                params['rule_amount'] = self.rule_amount
        if self.rule_discount:
            if hasattr(self.rule_discount, 'to_alipay_dict'):
                params['rule_discount'] = self.rule_discount.to_alipay_dict()
            else:
                params['rule_discount'] = self.rule_discount
        if self.rule_period:
            if hasattr(self.rule_period, 'to_alipay_dict'):
                params['rule_period'] = self.rule_period.to_alipay_dict()
            else:
                params['rule_period'] = self.rule_period
        if self.rule_period_unit:
            if hasattr(self.rule_period_unit, 'to_alipay_dict'):
                params['rule_period_unit'] = self.rule_period_unit.to_alipay_dict()
            else:
                params['rule_period_unit'] = self.rule_period_unit
        if self.rule_times:
            if hasattr(self.rule_times, 'to_alipay_dict'):
                params['rule_times'] = self.rule_times.to_alipay_dict()
            else:
                params['rule_times'] = self.rule_times
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivityRuleDetail()
        if 'rule_amount' in d:
            o.rule_amount = d['rule_amount']
        if 'rule_discount' in d:
            o.rule_discount = d['rule_discount']
        if 'rule_period' in d:
            o.rule_period = d['rule_period']
        if 'rule_period_unit' in d:
            o.rule_period_unit = d['rule_period_unit']
        if 'rule_times' in d:
            o.rule_times = d['rule_times']
        return o


