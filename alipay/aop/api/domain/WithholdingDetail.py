#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WithholdingDetail(object):

    def __init__(self):
        self._due_time = None
        self._last_payment_period = None
        self._period_number = None
        self._withholding_amount = None

    @property
    def due_time(self):
        return self._due_time

    @due_time.setter
    def due_time(self, value):
        self._due_time = value
    @property
    def last_payment_period(self):
        return self._last_payment_period

    @last_payment_period.setter
    def last_payment_period(self, value):
        self._last_payment_period = value
    @property
    def period_number(self):
        return self._period_number

    @period_number.setter
    def period_number(self, value):
        self._period_number = value
    @property
    def withholding_amount(self):
        return self._withholding_amount

    @withholding_amount.setter
    def withholding_amount(self, value):
        self._withholding_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.due_time:
            if hasattr(self.due_time, 'to_alipay_dict'):
                params['due_time'] = self.due_time.to_alipay_dict()
            else:
                params['due_time'] = self.due_time
        if self.last_payment_period:
            if hasattr(self.last_payment_period, 'to_alipay_dict'):
                params['last_payment_period'] = self.last_payment_period.to_alipay_dict()
            else:
                params['last_payment_period'] = self.last_payment_period
        if self.period_number:
            if hasattr(self.period_number, 'to_alipay_dict'):
                params['period_number'] = self.period_number.to_alipay_dict()
            else:
                params['period_number'] = self.period_number
        if self.withholding_amount:
            if hasattr(self.withholding_amount, 'to_alipay_dict'):
                params['withholding_amount'] = self.withholding_amount.to_alipay_dict()
            else:
                params['withholding_amount'] = self.withholding_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WithholdingDetail()
        if 'due_time' in d:
            o.due_time = d['due_time']
        if 'last_payment_period' in d:
            o.last_payment_period = d['last_payment_period']
        if 'period_number' in d:
            o.period_number = d['period_number']
        if 'withholding_amount' in d:
            o.withholding_amount = d['withholding_amount']
        return o


