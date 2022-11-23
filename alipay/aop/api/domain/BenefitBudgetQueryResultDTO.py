#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Amount import Amount
from alipay.aop.api.domain.Amount import Amount


class BenefitBudgetQueryResultDTO(object):

    def __init__(self):
        self._benefit_id = None
        self._budget_total_amount = None
        self._budget_total_count = None
        self._budget_type = None
        self._remain_amount = None
        self._remain_count = None

    @property
    def benefit_id(self):
        return self._benefit_id

    @benefit_id.setter
    def benefit_id(self, value):
        self._benefit_id = value
    @property
    def budget_total_amount(self):
        return self._budget_total_amount

    @budget_total_amount.setter
    def budget_total_amount(self, value):
        if isinstance(value, Amount):
            self._budget_total_amount = value
        else:
            self._budget_total_amount = Amount.from_alipay_dict(value)
    @property
    def budget_total_count(self):
        return self._budget_total_count

    @budget_total_count.setter
    def budget_total_count(self, value):
        self._budget_total_count = value
    @property
    def budget_type(self):
        return self._budget_type

    @budget_type.setter
    def budget_type(self, value):
        self._budget_type = value
    @property
    def remain_amount(self):
        return self._remain_amount

    @remain_amount.setter
    def remain_amount(self, value):
        if isinstance(value, Amount):
            self._remain_amount = value
        else:
            self._remain_amount = Amount.from_alipay_dict(value)
    @property
    def remain_count(self):
        return self._remain_count

    @remain_count.setter
    def remain_count(self, value):
        self._remain_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_id:
            if hasattr(self.benefit_id, 'to_alipay_dict'):
                params['benefit_id'] = self.benefit_id.to_alipay_dict()
            else:
                params['benefit_id'] = self.benefit_id
        if self.budget_total_amount:
            if hasattr(self.budget_total_amount, 'to_alipay_dict'):
                params['budget_total_amount'] = self.budget_total_amount.to_alipay_dict()
            else:
                params['budget_total_amount'] = self.budget_total_amount
        if self.budget_total_count:
            if hasattr(self.budget_total_count, 'to_alipay_dict'):
                params['budget_total_count'] = self.budget_total_count.to_alipay_dict()
            else:
                params['budget_total_count'] = self.budget_total_count
        if self.budget_type:
            if hasattr(self.budget_type, 'to_alipay_dict'):
                params['budget_type'] = self.budget_type.to_alipay_dict()
            else:
                params['budget_type'] = self.budget_type
        if self.remain_amount:
            if hasattr(self.remain_amount, 'to_alipay_dict'):
                params['remain_amount'] = self.remain_amount.to_alipay_dict()
            else:
                params['remain_amount'] = self.remain_amount
        if self.remain_count:
            if hasattr(self.remain_count, 'to_alipay_dict'):
                params['remain_count'] = self.remain_count.to_alipay_dict()
            else:
                params['remain_count'] = self.remain_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitBudgetQueryResultDTO()
        if 'benefit_id' in d:
            o.benefit_id = d['benefit_id']
        if 'budget_total_amount' in d:
            o.budget_total_amount = d['budget_total_amount']
        if 'budget_total_count' in d:
            o.budget_total_count = d['budget_total_count']
        if 'budget_type' in d:
            o.budget_type = d['budget_type']
        if 'remain_amount' in d:
            o.remain_amount = d['remain_amount']
        if 'remain_count' in d:
            o.remain_count = d['remain_count']
        return o


