#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BenefitAccountFundBudgetInfoDTO(object):

    def __init__(self):
        self._back_budget = None
        self._back_cash = None
        self._in_budget = None
        self._in_cash = None

    @property
    def back_budget(self):
        return self._back_budget

    @back_budget.setter
    def back_budget(self, value):
        self._back_budget = value
    @property
    def back_cash(self):
        return self._back_cash

    @back_cash.setter
    def back_cash(self, value):
        self._back_cash = value
    @property
    def in_budget(self):
        return self._in_budget

    @in_budget.setter
    def in_budget(self, value):
        self._in_budget = value
    @property
    def in_cash(self):
        return self._in_cash

    @in_cash.setter
    def in_cash(self, value):
        self._in_cash = value


    def to_alipay_dict(self):
        params = dict()
        if self.back_budget:
            if hasattr(self.back_budget, 'to_alipay_dict'):
                params['back_budget'] = self.back_budget.to_alipay_dict()
            else:
                params['back_budget'] = self.back_budget
        if self.back_cash:
            if hasattr(self.back_cash, 'to_alipay_dict'):
                params['back_cash'] = self.back_cash.to_alipay_dict()
            else:
                params['back_cash'] = self.back_cash
        if self.in_budget:
            if hasattr(self.in_budget, 'to_alipay_dict'):
                params['in_budget'] = self.in_budget.to_alipay_dict()
            else:
                params['in_budget'] = self.in_budget
        if self.in_cash:
            if hasattr(self.in_cash, 'to_alipay_dict'):
                params['in_cash'] = self.in_cash.to_alipay_dict()
            else:
                params['in_cash'] = self.in_cash
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitAccountFundBudgetInfoDTO()
        if 'back_budget' in d:
            o.back_budget = d['back_budget']
        if 'back_cash' in d:
            o.back_cash = d['back_cash']
        if 'in_budget' in d:
            o.in_budget = d['in_budget']
        if 'in_cash' in d:
            o.in_cash = d['in_cash']
        return o


