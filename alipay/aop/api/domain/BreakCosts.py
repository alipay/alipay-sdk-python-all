#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BreakCosts(object):

    def __init__(self):
        self._break_costs_rate = None
        self._break_costs_type = None

    @property
    def break_costs_rate(self):
        return self._break_costs_rate

    @break_costs_rate.setter
    def break_costs_rate(self, value):
        self._break_costs_rate = value
    @property
    def break_costs_type(self):
        return self._break_costs_type

    @break_costs_type.setter
    def break_costs_type(self, value):
        self._break_costs_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.break_costs_rate:
            if hasattr(self.break_costs_rate, 'to_alipay_dict'):
                params['break_costs_rate'] = self.break_costs_rate.to_alipay_dict()
            else:
                params['break_costs_rate'] = self.break_costs_rate
        if self.break_costs_type:
            if hasattr(self.break_costs_type, 'to_alipay_dict'):
                params['break_costs_type'] = self.break_costs_type.to_alipay_dict()
            else:
                params['break_costs_type'] = self.break_costs_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BreakCosts()
        if 'break_costs_rate' in d:
            o.break_costs_rate = d['break_costs_rate']
        if 'break_costs_type' in d:
            o.break_costs_type = d['break_costs_type']
        return o


