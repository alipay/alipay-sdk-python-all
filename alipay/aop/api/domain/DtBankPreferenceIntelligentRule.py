#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DtBankPreferenceIntelligentRule(object):

    def __init__(self):
        self._max_amount = None
        self._min_amount = None
        self._optimization_target = None

    @property
    def max_amount(self):
        return self._max_amount

    @max_amount.setter
    def max_amount(self, value):
        self._max_amount = value
    @property
    def min_amount(self):
        return self._min_amount

    @min_amount.setter
    def min_amount(self, value):
        self._min_amount = value
    @property
    def optimization_target(self):
        return self._optimization_target

    @optimization_target.setter
    def optimization_target(self, value):
        self._optimization_target = value


    def to_alipay_dict(self):
        params = dict()
        if self.max_amount:
            if hasattr(self.max_amount, 'to_alipay_dict'):
                params['max_amount'] = self.max_amount.to_alipay_dict()
            else:
                params['max_amount'] = self.max_amount
        if self.min_amount:
            if hasattr(self.min_amount, 'to_alipay_dict'):
                params['min_amount'] = self.min_amount.to_alipay_dict()
            else:
                params['min_amount'] = self.min_amount
        if self.optimization_target:
            if hasattr(self.optimization_target, 'to_alipay_dict'):
                params['optimization_target'] = self.optimization_target.to_alipay_dict()
            else:
                params['optimization_target'] = self.optimization_target
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DtBankPreferenceIntelligentRule()
        if 'max_amount' in d:
            o.max_amount = d['max_amount']
        if 'min_amount' in d:
            o.min_amount = d['min_amount']
        if 'optimization_target' in d:
            o.optimization_target = d['optimization_target']
        return o


