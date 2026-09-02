#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentPayInfo(object):

    def __init__(self):
        self._end_date = None
        self._pay_amount = None
        self._pay_date = None
        self._pay_periods = None
        self._start_date = None

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_date(self):
        return self._pay_date

    @pay_date.setter
    def pay_date(self, value):
        self._pay_date = value
    @property
    def pay_periods(self):
        return self._pay_periods

    @pay_periods.setter
    def pay_periods(self, value):
        self._pay_periods = value
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
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.pay_date:
            if hasattr(self.pay_date, 'to_alipay_dict'):
                params['pay_date'] = self.pay_date.to_alipay_dict()
            else:
                params['pay_date'] = self.pay_date
        if self.pay_periods:
            if hasattr(self.pay_periods, 'to_alipay_dict'):
                params['pay_periods'] = self.pay_periods.to_alipay_dict()
            else:
                params['pay_periods'] = self.pay_periods
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
        o = RentPayInfo()
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'pay_date' in d:
            o.pay_date = d['pay_date']
        if 'pay_periods' in d:
            o.pay_periods = d['pay_periods']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


