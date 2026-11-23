#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PrepayPeriodAmount(object):

    def __init__(self):
        self._amount = None
        self._months = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def months(self):
        return self._months

    @months.setter
    def months(self, value):
        self._months = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.months:
            if hasattr(self.months, 'to_alipay_dict'):
                params['months'] = self.months.to_alipay_dict()
            else:
                params['months'] = self.months
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PrepayPeriodAmount()
        if 'amount' in d:
            o.amount = d['amount']
        if 'months' in d:
            o.months = d['months']
        return o


