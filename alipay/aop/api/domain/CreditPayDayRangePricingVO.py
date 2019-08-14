#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreditPayDayRangePricingVO(object):

    def __init__(self):
        self._end_date = None
        self._int_rate = None
        self._interest = None
        self._start_date = None

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def int_rate(self):
        return self._int_rate

    @int_rate.setter
    def int_rate(self, value):
        self._int_rate = value
    @property
    def interest(self):
        return self._interest

    @interest.setter
    def interest(self, value):
        self._interest = value
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
        if self.int_rate:
            if hasattr(self.int_rate, 'to_alipay_dict'):
                params['int_rate'] = self.int_rate.to_alipay_dict()
            else:
                params['int_rate'] = self.int_rate
        if self.interest:
            if hasattr(self.interest, 'to_alipay_dict'):
                params['interest'] = self.interest.to_alipay_dict()
            else:
                params['interest'] = self.interest
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
        o = CreditPayDayRangePricingVO()
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'int_rate' in d:
            o.int_rate = d['int_rate']
        if 'interest' in d:
            o.interest = d['interest']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


