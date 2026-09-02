#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BankQuotaResult(object):

    def __init__(self):
        self._limit_amount = None
        self._quota_month = None
        self._remaining_amount = None

    @property
    def limit_amount(self):
        return self._limit_amount

    @limit_amount.setter
    def limit_amount(self, value):
        self._limit_amount = value
    @property
    def quota_month(self):
        return self._quota_month

    @quota_month.setter
    def quota_month(self, value):
        self._quota_month = value
    @property
    def remaining_amount(self):
        return self._remaining_amount

    @remaining_amount.setter
    def remaining_amount(self, value):
        self._remaining_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.limit_amount:
            if hasattr(self.limit_amount, 'to_alipay_dict'):
                params['limit_amount'] = self.limit_amount.to_alipay_dict()
            else:
                params['limit_amount'] = self.limit_amount
        if self.quota_month:
            if hasattr(self.quota_month, 'to_alipay_dict'):
                params['quota_month'] = self.quota_month.to_alipay_dict()
            else:
                params['quota_month'] = self.quota_month
        if self.remaining_amount:
            if hasattr(self.remaining_amount, 'to_alipay_dict'):
                params['remaining_amount'] = self.remaining_amount.to_alipay_dict()
            else:
                params['remaining_amount'] = self.remaining_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BankQuotaResult()
        if 'limit_amount' in d:
            o.limit_amount = d['limit_amount']
        if 'quota_month' in d:
            o.quota_month = d['quota_month']
        if 'remaining_amount' in d:
            o.remaining_amount = d['remaining_amount']
        return o


