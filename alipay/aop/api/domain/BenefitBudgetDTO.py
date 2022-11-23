#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Amount import Amount


class BenefitBudgetDTO(object):

    def __init__(self):
        self._amount = None
        self._budget_type = None
        self._count = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if isinstance(value, Amount):
            self._amount = value
        else:
            self._amount = Amount.from_alipay_dict(value)
    @property
    def budget_type(self):
        return self._budget_type

    @budget_type.setter
    def budget_type(self, value):
        self._budget_type = value
    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.budget_type:
            if hasattr(self.budget_type, 'to_alipay_dict'):
                params['budget_type'] = self.budget_type.to_alipay_dict()
            else:
                params['budget_type'] = self.budget_type
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitBudgetDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'budget_type' in d:
            o.budget_type = d['budget_type']
        if 'count' in d:
            o.count = d['count']
        return o


