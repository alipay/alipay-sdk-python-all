#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BudgetInfo(object):

    def __init__(self):
        self._budget_total = None
        self._budget_type = None
        self._sub_budget_dimension = None
        self._sub_value = None

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
    @property
    def sub_budget_dimension(self):
        return self._sub_budget_dimension

    @sub_budget_dimension.setter
    def sub_budget_dimension(self, value):
        self._sub_budget_dimension = value
    @property
    def sub_value(self):
        return self._sub_value

    @sub_value.setter
    def sub_value(self, value):
        self._sub_value = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.sub_budget_dimension:
            if hasattr(self.sub_budget_dimension, 'to_alipay_dict'):
                params['sub_budget_dimension'] = self.sub_budget_dimension.to_alipay_dict()
            else:
                params['sub_budget_dimension'] = self.sub_budget_dimension
        if self.sub_value:
            if hasattr(self.sub_value, 'to_alipay_dict'):
                params['sub_value'] = self.sub_value.to_alipay_dict()
            else:
                params['sub_value'] = self.sub_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BudgetInfo()
        if 'budget_total' in d:
            o.budget_total = d['budget_total']
        if 'budget_type' in d:
            o.budget_type = d['budget_type']
        if 'sub_budget_dimension' in d:
            o.sub_budget_dimension = d['sub_budget_dimension']
        if 'sub_value' in d:
            o.sub_value = d['sub_value']
        return o


