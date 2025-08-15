#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PaymentLogVo(object):

    def __init__(self):
        self._end_date = None
        self._expense_amount = None
        self._expense_count = None
        self._income_amount = None
        self._income_count = None
        self._start_date = None

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def expense_amount(self):
        return self._expense_amount

    @expense_amount.setter
    def expense_amount(self, value):
        self._expense_amount = value
    @property
    def expense_count(self):
        return self._expense_count

    @expense_count.setter
    def expense_count(self, value):
        self._expense_count = value
    @property
    def income_amount(self):
        return self._income_amount

    @income_amount.setter
    def income_amount(self, value):
        self._income_amount = value
    @property
    def income_count(self):
        return self._income_count

    @income_count.setter
    def income_count(self, value):
        self._income_count = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.expense_amount:
            if hasattr(self.expense_amount, 'to_alipay_dict'):
                params['expense_amount'] = self.expense_amount.to_alipay_dict()
            else:
                params['expense_amount'] = self.expense_amount
        if self.expense_count:
            if hasattr(self.expense_count, 'to_alipay_dict'):
                params['expense_count'] = self.expense_count.to_alipay_dict()
            else:
                params['expense_count'] = self.expense_count
        if self.income_amount:
            if hasattr(self.income_amount, 'to_alipay_dict'):
                params['income_amount'] = self.income_amount.to_alipay_dict()
            else:
                params['income_amount'] = self.income_amount
        if self.income_count:
            if hasattr(self.income_count, 'to_alipay_dict'):
                params['income_count'] = self.income_count.to_alipay_dict()
            else:
                params['income_count'] = self.income_count
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaymentLogVo()
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'expense_amount' in d:
            o.expense_amount = d['expense_amount']
        if 'expense_count' in d:
            o.expense_count = d['expense_count']
        if 'income_amount' in d:
            o.income_amount = d['income_amount']
        if 'income_count' in d:
            o.income_count = d['income_count']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


