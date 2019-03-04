#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MBudgetInfo(object):

    def __init__(self):
        self._budget_daily = None
        self._budget_total = None
        self._budget_type = None

    @property
    def budget_daily(self):
        return self._budget_daily

    @budget_daily.setter
    def budget_daily(self, value):
        self._budget_daily = value
    @property
    def budget_total(self):
        return self._budget_total

    @budget_total.setter
    def budget_total(self, value):
        self._budget_total = value
    @property
    def budget_type(self):
        return self._budget_type

    @budget_type.setter
    def budget_type(self, value):
        self._budget_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.budget_daily:
            if hasattr(self.budget_daily, 'to_alipay_dict'):
                params['budget_daily'] = self.budget_daily.to_alipay_dict()
            else:
                params['budget_daily'] = self.budget_daily
        if self.budget_total:
            if hasattr(self.budget_total, 'to_alipay_dict'):
                params['budget_total'] = self.budget_total.to_alipay_dict()
            else:
                params['budget_total'] = self.budget_total
        if self.budget_type:
            if hasattr(self.budget_type, 'to_alipay_dict'):
                params['budget_type'] = self.budget_type.to_alipay_dict()
            else:
                params['budget_type'] = self.budget_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MBudgetInfo()
        if 'budget_daily' in d:
            o.budget_daily = d['budget_daily']
        if 'budget_total' in d:
            o.budget_total = d['budget_total']
        if 'budget_type' in d:
            o.budget_type = d['budget_type']
        return o


