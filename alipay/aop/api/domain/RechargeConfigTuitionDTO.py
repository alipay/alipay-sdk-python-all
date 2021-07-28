#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RechargeConfigTuitionDTO(object):

    def __init__(self):
        self._ext_info = None
        self._first_payment_time = None
        self._interval = None
        self._last_payment_time = None
        self._period_type = None
        self._periods = None
        self._total_amount = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def first_payment_time(self):
        return self._first_payment_time

    @first_payment_time.setter
    def first_payment_time(self, value):
        self._first_payment_time = value
    @property
    def interval(self):
        return self._interval

    @interval.setter
    def interval(self, value):
        self._interval = value
    @property
    def last_payment_time(self):
        return self._last_payment_time

    @last_payment_time.setter
    def last_payment_time(self, value):
        self._last_payment_time = value
    @property
    def period_type(self):
        return self._period_type

    @period_type.setter
    def period_type(self, value):
        self._period_type = value
    @property
    def periods(self):
        return self._periods

    @periods.setter
    def periods(self, value):
        self._periods = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.first_payment_time:
            if hasattr(self.first_payment_time, 'to_alipay_dict'):
                params['first_payment_time'] = self.first_payment_time.to_alipay_dict()
            else:
                params['first_payment_time'] = self.first_payment_time
        if self.interval:
            if hasattr(self.interval, 'to_alipay_dict'):
                params['interval'] = self.interval.to_alipay_dict()
            else:
                params['interval'] = self.interval
        if self.last_payment_time:
            if hasattr(self.last_payment_time, 'to_alipay_dict'):
                params['last_payment_time'] = self.last_payment_time.to_alipay_dict()
            else:
                params['last_payment_time'] = self.last_payment_time
        if self.period_type:
            if hasattr(self.period_type, 'to_alipay_dict'):
                params['period_type'] = self.period_type.to_alipay_dict()
            else:
                params['period_type'] = self.period_type
        if self.periods:
            if hasattr(self.periods, 'to_alipay_dict'):
                params['periods'] = self.periods.to_alipay_dict()
            else:
                params['periods'] = self.periods
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RechargeConfigTuitionDTO()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'first_payment_time' in d:
            o.first_payment_time = d['first_payment_time']
        if 'interval' in d:
            o.interval = d['interval']
        if 'last_payment_time' in d:
            o.last_payment_time = d['last_payment_time']
        if 'period_type' in d:
            o.period_type = d['period_type']
        if 'periods' in d:
            o.periods = d['periods']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


