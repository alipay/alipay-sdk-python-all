#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CycleAvgDiscountAmountConfig import CycleAvgDiscountAmountConfig


class DtBankPreferenceIntelligentRule(object):

    def __init__(self):
        self._avg_discount_amount = None
        self._avg_discount_amount_type = None
        self._cycle_avg_discount_amount_config_list = None
        self._max_amount = None
        self._min_amount = None
        self._optimization_target = None

    @property
    def avg_discount_amount(self):
        return self._avg_discount_amount

    @avg_discount_amount.setter
    def avg_discount_amount(self, value):
        self._avg_discount_amount = value
    @property
    def avg_discount_amount_type(self):
        return self._avg_discount_amount_type

    @avg_discount_amount_type.setter
    def avg_discount_amount_type(self, value):
        self._avg_discount_amount_type = value
    @property
    def cycle_avg_discount_amount_config_list(self):
        return self._cycle_avg_discount_amount_config_list

    @cycle_avg_discount_amount_config_list.setter
    def cycle_avg_discount_amount_config_list(self, value):
        if isinstance(value, list):
            self._cycle_avg_discount_amount_config_list = list()
            for i in value:
                if isinstance(i, CycleAvgDiscountAmountConfig):
                    self._cycle_avg_discount_amount_config_list.append(i)
                else:
                    self._cycle_avg_discount_amount_config_list.append(CycleAvgDiscountAmountConfig.from_alipay_dict(i))
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
        if self.avg_discount_amount:
            if hasattr(self.avg_discount_amount, 'to_alipay_dict'):
                params['avg_discount_amount'] = self.avg_discount_amount.to_alipay_dict()
            else:
                params['avg_discount_amount'] = self.avg_discount_amount
        if self.avg_discount_amount_type:
            if hasattr(self.avg_discount_amount_type, 'to_alipay_dict'):
                params['avg_discount_amount_type'] = self.avg_discount_amount_type.to_alipay_dict()
            else:
                params['avg_discount_amount_type'] = self.avg_discount_amount_type
        if self.cycle_avg_discount_amount_config_list:
            if isinstance(self.cycle_avg_discount_amount_config_list, list):
                for i in range(0, len(self.cycle_avg_discount_amount_config_list)):
                    element = self.cycle_avg_discount_amount_config_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cycle_avg_discount_amount_config_list[i] = element.to_alipay_dict()
            if hasattr(self.cycle_avg_discount_amount_config_list, 'to_alipay_dict'):
                params['cycle_avg_discount_amount_config_list'] = self.cycle_avg_discount_amount_config_list.to_alipay_dict()
            else:
                params['cycle_avg_discount_amount_config_list'] = self.cycle_avg_discount_amount_config_list
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
        if 'avg_discount_amount' in d:
            o.avg_discount_amount = d['avg_discount_amount']
        if 'avg_discount_amount_type' in d:
            o.avg_discount_amount_type = d['avg_discount_amount_type']
        if 'cycle_avg_discount_amount_config_list' in d:
            o.cycle_avg_discount_amount_config_list = d['cycle_avg_discount_amount_config_list']
        if 'max_amount' in d:
            o.max_amount = d['max_amount']
        if 'min_amount' in d:
            o.min_amount = d['min_amount']
        if 'optimization_target' in d:
            o.optimization_target = d['optimization_target']
        return o


