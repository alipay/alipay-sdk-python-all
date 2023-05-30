#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DtBankBudgetRealTimeInfo(object):

    def __init__(self):
        self._refund_amount = None
        self._remaining_budget = None
        self._send_amount = None
        self._send_count = None
        self._used_amount = None
        self._used_count = None

    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def remaining_budget(self):
        return self._remaining_budget

    @remaining_budget.setter
    def remaining_budget(self, value):
        self._remaining_budget = value
    @property
    def send_amount(self):
        return self._send_amount

    @send_amount.setter
    def send_amount(self, value):
        self._send_amount = value
    @property
    def send_count(self):
        return self._send_count

    @send_count.setter
    def send_count(self, value):
        self._send_count = value
    @property
    def used_amount(self):
        return self._used_amount

    @used_amount.setter
    def used_amount(self, value):
        self._used_amount = value
    @property
    def used_count(self):
        return self._used_count

    @used_count.setter
    def used_count(self, value):
        self._used_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.remaining_budget:
            if hasattr(self.remaining_budget, 'to_alipay_dict'):
                params['remaining_budget'] = self.remaining_budget.to_alipay_dict()
            else:
                params['remaining_budget'] = self.remaining_budget
        if self.send_amount:
            if hasattr(self.send_amount, 'to_alipay_dict'):
                params['send_amount'] = self.send_amount.to_alipay_dict()
            else:
                params['send_amount'] = self.send_amount
        if self.send_count:
            if hasattr(self.send_count, 'to_alipay_dict'):
                params['send_count'] = self.send_count.to_alipay_dict()
            else:
                params['send_count'] = self.send_count
        if self.used_amount:
            if hasattr(self.used_amount, 'to_alipay_dict'):
                params['used_amount'] = self.used_amount.to_alipay_dict()
            else:
                params['used_amount'] = self.used_amount
        if self.used_count:
            if hasattr(self.used_count, 'to_alipay_dict'):
                params['used_count'] = self.used_count.to_alipay_dict()
            else:
                params['used_count'] = self.used_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DtBankBudgetRealTimeInfo()
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'remaining_budget' in d:
            o.remaining_budget = d['remaining_budget']
        if 'send_amount' in d:
            o.send_amount = d['send_amount']
        if 'send_count' in d:
            o.send_count = d['send_count']
        if 'used_amount' in d:
            o.used_amount = d['used_amount']
        if 'used_count' in d:
            o.used_count = d['used_count']
        return o


