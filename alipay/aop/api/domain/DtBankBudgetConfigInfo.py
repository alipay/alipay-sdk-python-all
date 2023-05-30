#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DtBankBudgetConfigInfo(object):

    def __init__(self):
        self._daily_budget_type = None
        self._daily_budget_value = None
        self._min_send_count = None
        self._total_budget = None

    @property
    def daily_budget_type(self):
        return self._daily_budget_type

    @daily_budget_type.setter
    def daily_budget_type(self, value):
        self._daily_budget_type = value
    @property
    def daily_budget_value(self):
        return self._daily_budget_value

    @daily_budget_value.setter
    def daily_budget_value(self, value):
        self._daily_budget_value = value
    @property
    def min_send_count(self):
        return self._min_send_count

    @min_send_count.setter
    def min_send_count(self, value):
        self._min_send_count = value
    @property
    def total_budget(self):
        return self._total_budget

    @total_budget.setter
    def total_budget(self, value):
        self._total_budget = value


    def to_alipay_dict(self):
        params = dict()
        if self.daily_budget_type:
            if hasattr(self.daily_budget_type, 'to_alipay_dict'):
                params['daily_budget_type'] = self.daily_budget_type.to_alipay_dict()
            else:
                params['daily_budget_type'] = self.daily_budget_type
        if self.daily_budget_value:
            if hasattr(self.daily_budget_value, 'to_alipay_dict'):
                params['daily_budget_value'] = self.daily_budget_value.to_alipay_dict()
            else:
                params['daily_budget_value'] = self.daily_budget_value
        if self.min_send_count:
            if hasattr(self.min_send_count, 'to_alipay_dict'):
                params['min_send_count'] = self.min_send_count.to_alipay_dict()
            else:
                params['min_send_count'] = self.min_send_count
        if self.total_budget:
            if hasattr(self.total_budget, 'to_alipay_dict'):
                params['total_budget'] = self.total_budget.to_alipay_dict()
            else:
                params['total_budget'] = self.total_budget
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DtBankBudgetConfigInfo()
        if 'daily_budget_type' in d:
            o.daily_budget_type = d['daily_budget_type']
        if 'daily_budget_value' in d:
            o.daily_budget_value = d['daily_budget_value']
        if 'min_send_count' in d:
            o.min_send_count = d['min_send_count']
        if 'total_budget' in d:
            o.total_budget = d['total_budget']
        return o


