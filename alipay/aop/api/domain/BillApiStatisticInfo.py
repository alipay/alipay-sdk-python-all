#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BillApiStatisticInfo(object):

    def __init__(self):
        self._expenditure_amount = None
        self._income_amount = None

    @property
    def expenditure_amount(self):
        return self._expenditure_amount

    @expenditure_amount.setter
    def expenditure_amount(self, value):
        self._expenditure_amount = value
    @property
    def income_amount(self):
        return self._income_amount

    @income_amount.setter
    def income_amount(self, value):
        self._income_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.expenditure_amount:
            if hasattr(self.expenditure_amount, 'to_alipay_dict'):
                params['expenditure_amount'] = self.expenditure_amount.to_alipay_dict()
            else:
                params['expenditure_amount'] = self.expenditure_amount
        if self.income_amount:
            if hasattr(self.income_amount, 'to_alipay_dict'):
                params['income_amount'] = self.income_amount.to_alipay_dict()
            else:
                params['income_amount'] = self.income_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BillApiStatisticInfo()
        if 'expenditure_amount' in d:
            o.expenditure_amount = d['expenditure_amount']
        if 'income_amount' in d:
            o.income_amount = d['income_amount']
        return o


