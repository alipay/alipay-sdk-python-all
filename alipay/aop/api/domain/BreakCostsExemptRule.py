#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BreakCostsExemptRule(object):

    def __init__(self):
        self._break_costs_7_days = None
        self._break_costs_expired = None
        self._no_break_costs_flag = None
        self._no_break_costs_standard_value = None

    @property
    def break_costs_7_days(self):
        return self._break_costs_7_days

    @break_costs_7_days.setter
    def break_costs_7_days(self, value):
        self._break_costs_7_days = value
    @property
    def break_costs_expired(self):
        return self._break_costs_expired

    @break_costs_expired.setter
    def break_costs_expired(self, value):
        self._break_costs_expired = value
    @property
    def no_break_costs_flag(self):
        return self._no_break_costs_flag

    @no_break_costs_flag.setter
    def no_break_costs_flag(self, value):
        self._no_break_costs_flag = value
    @property
    def no_break_costs_standard_value(self):
        return self._no_break_costs_standard_value

    @no_break_costs_standard_value.setter
    def no_break_costs_standard_value(self, value):
        self._no_break_costs_standard_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.break_costs_7_days:
            if hasattr(self.break_costs_7_days, 'to_alipay_dict'):
                params['break_costs_7_days'] = self.break_costs_7_days.to_alipay_dict()
            else:
                params['break_costs_7_days'] = self.break_costs_7_days
        if self.break_costs_expired:
            if hasattr(self.break_costs_expired, 'to_alipay_dict'):
                params['break_costs_expired'] = self.break_costs_expired.to_alipay_dict()
            else:
                params['break_costs_expired'] = self.break_costs_expired
        if self.no_break_costs_flag:
            if hasattr(self.no_break_costs_flag, 'to_alipay_dict'):
                params['no_break_costs_flag'] = self.no_break_costs_flag.to_alipay_dict()
            else:
                params['no_break_costs_flag'] = self.no_break_costs_flag
        if self.no_break_costs_standard_value:
            if hasattr(self.no_break_costs_standard_value, 'to_alipay_dict'):
                params['no_break_costs_standard_value'] = self.no_break_costs_standard_value.to_alipay_dict()
            else:
                params['no_break_costs_standard_value'] = self.no_break_costs_standard_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BreakCostsExemptRule()
        if 'break_costs_7_days' in d:
            o.break_costs_7_days = d['break_costs_7_days']
        if 'break_costs_expired' in d:
            o.break_costs_expired = d['break_costs_expired']
        if 'no_break_costs_flag' in d:
            o.no_break_costs_flag = d['no_break_costs_flag']
        if 'no_break_costs_standard_value' in d:
            o.no_break_costs_standard_value = d['no_break_costs_standard_value']
        return o


