#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BillDingBizOrderSum(object):

    def __init__(self):
        self._biz_date = None
        self._expenses = None
        self._income = None

    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def expenses(self):
        return self._expenses

    @expenses.setter
    def expenses(self, value):
        self._expenses = value
    @property
    def income(self):
        return self._income

    @income.setter
    def income(self, value):
        self._income = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        if self.expenses:
            if hasattr(self.expenses, 'to_alipay_dict'):
                params['expenses'] = self.expenses.to_alipay_dict()
            else:
                params['expenses'] = self.expenses
        if self.income:
            if hasattr(self.income, 'to_alipay_dict'):
                params['income'] = self.income.to_alipay_dict()
            else:
                params['income'] = self.income
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BillDingBizOrderSum()
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'expenses' in d:
            o.expenses = d['expenses']
        if 'income' in d:
            o.income = d['income']
        return o


