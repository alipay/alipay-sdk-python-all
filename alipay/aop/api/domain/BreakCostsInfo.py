#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BreakCostsInfo(object):

    def __init__(self):
        self._break_costs_expired = None
        self._break_costs_seven_days = None
        self._damages_rate = None
        self._damages_type = None
        self._no_break_costs_flag = None
        self._no_break_costs_unit = None
        self._no_break_costs_value = None

    @property
    def break_costs_expired(self):
        return self._break_costs_expired

    @break_costs_expired.setter
    def break_costs_expired(self, value):
        self._break_costs_expired = value
    @property
    def break_costs_seven_days(self):
        return self._break_costs_seven_days

    @break_costs_seven_days.setter
    def break_costs_seven_days(self, value):
        self._break_costs_seven_days = value
    @property
    def damages_rate(self):
        return self._damages_rate

    @damages_rate.setter
    def damages_rate(self, value):
        self._damages_rate = value
    @property
    def damages_type(self):
        return self._damages_type

    @damages_type.setter
    def damages_type(self, value):
        self._damages_type = value
    @property
    def no_break_costs_flag(self):
        return self._no_break_costs_flag

    @no_break_costs_flag.setter
    def no_break_costs_flag(self, value):
        self._no_break_costs_flag = value
    @property
    def no_break_costs_unit(self):
        return self._no_break_costs_unit

    @no_break_costs_unit.setter
    def no_break_costs_unit(self, value):
        self._no_break_costs_unit = value
    @property
    def no_break_costs_value(self):
        return self._no_break_costs_value

    @no_break_costs_value.setter
    def no_break_costs_value(self, value):
        self._no_break_costs_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.break_costs_expired:
            if hasattr(self.break_costs_expired, 'to_alipay_dict'):
                params['break_costs_expired'] = self.break_costs_expired.to_alipay_dict()
            else:
                params['break_costs_expired'] = self.break_costs_expired
        if self.break_costs_seven_days:
            if hasattr(self.break_costs_seven_days, 'to_alipay_dict'):
                params['break_costs_seven_days'] = self.break_costs_seven_days.to_alipay_dict()
            else:
                params['break_costs_seven_days'] = self.break_costs_seven_days
        if self.damages_rate:
            if hasattr(self.damages_rate, 'to_alipay_dict'):
                params['damages_rate'] = self.damages_rate.to_alipay_dict()
            else:
                params['damages_rate'] = self.damages_rate
        if self.damages_type:
            if hasattr(self.damages_type, 'to_alipay_dict'):
                params['damages_type'] = self.damages_type.to_alipay_dict()
            else:
                params['damages_type'] = self.damages_type
        if self.no_break_costs_flag:
            if hasattr(self.no_break_costs_flag, 'to_alipay_dict'):
                params['no_break_costs_flag'] = self.no_break_costs_flag.to_alipay_dict()
            else:
                params['no_break_costs_flag'] = self.no_break_costs_flag
        if self.no_break_costs_unit:
            if hasattr(self.no_break_costs_unit, 'to_alipay_dict'):
                params['no_break_costs_unit'] = self.no_break_costs_unit.to_alipay_dict()
            else:
                params['no_break_costs_unit'] = self.no_break_costs_unit
        if self.no_break_costs_value:
            if hasattr(self.no_break_costs_value, 'to_alipay_dict'):
                params['no_break_costs_value'] = self.no_break_costs_value.to_alipay_dict()
            else:
                params['no_break_costs_value'] = self.no_break_costs_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BreakCostsInfo()
        if 'break_costs_expired' in d:
            o.break_costs_expired = d['break_costs_expired']
        if 'break_costs_seven_days' in d:
            o.break_costs_seven_days = d['break_costs_seven_days']
        if 'damages_rate' in d:
            o.damages_rate = d['damages_rate']
        if 'damages_type' in d:
            o.damages_type = d['damages_type']
        if 'no_break_costs_flag' in d:
            o.no_break_costs_flag = d['no_break_costs_flag']
        if 'no_break_costs_unit' in d:
            o.no_break_costs_unit = d['no_break_costs_unit']
        if 'no_break_costs_value' in d:
            o.no_break_costs_value = d['no_break_costs_value']
        return o


