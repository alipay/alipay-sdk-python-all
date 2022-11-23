#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RndBenefitRule import RndBenefitRule


class VcpCalcFormula(object):

    def __init__(self):
        self._base_count = None
        self._max_count = None
        self._reduction_amount = None
        self._reduction_ratio = None
        self._rnd_benefit_rules = None
        self._rounding_mode = None
        self._specified_amount = None

    @property
    def base_count(self):
        return self._base_count

    @base_count.setter
    def base_count(self, value):
        self._base_count = value
    @property
    def max_count(self):
        return self._max_count

    @max_count.setter
    def max_count(self, value):
        self._max_count = value
    @property
    def reduction_amount(self):
        return self._reduction_amount

    @reduction_amount.setter
    def reduction_amount(self, value):
        self._reduction_amount = value
    @property
    def reduction_ratio(self):
        return self._reduction_ratio

    @reduction_ratio.setter
    def reduction_ratio(self, value):
        self._reduction_ratio = value
    @property
    def rnd_benefit_rules(self):
        return self._rnd_benefit_rules

    @rnd_benefit_rules.setter
    def rnd_benefit_rules(self, value):
        if isinstance(value, list):
            self._rnd_benefit_rules = list()
            for i in value:
                if isinstance(i, RndBenefitRule):
                    self._rnd_benefit_rules.append(i)
                else:
                    self._rnd_benefit_rules.append(RndBenefitRule.from_alipay_dict(i))
    @property
    def rounding_mode(self):
        return self._rounding_mode

    @rounding_mode.setter
    def rounding_mode(self, value):
        self._rounding_mode = value
    @property
    def specified_amount(self):
        return self._specified_amount

    @specified_amount.setter
    def specified_amount(self, value):
        self._specified_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.base_count:
            if hasattr(self.base_count, 'to_alipay_dict'):
                params['base_count'] = self.base_count.to_alipay_dict()
            else:
                params['base_count'] = self.base_count
        if self.max_count:
            if hasattr(self.max_count, 'to_alipay_dict'):
                params['max_count'] = self.max_count.to_alipay_dict()
            else:
                params['max_count'] = self.max_count
        if self.reduction_amount:
            if hasattr(self.reduction_amount, 'to_alipay_dict'):
                params['reduction_amount'] = self.reduction_amount.to_alipay_dict()
            else:
                params['reduction_amount'] = self.reduction_amount
        if self.reduction_ratio:
            if hasattr(self.reduction_ratio, 'to_alipay_dict'):
                params['reduction_ratio'] = self.reduction_ratio.to_alipay_dict()
            else:
                params['reduction_ratio'] = self.reduction_ratio
        if self.rnd_benefit_rules:
            if isinstance(self.rnd_benefit_rules, list):
                for i in range(0, len(self.rnd_benefit_rules)):
                    element = self.rnd_benefit_rules[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rnd_benefit_rules[i] = element.to_alipay_dict()
            if hasattr(self.rnd_benefit_rules, 'to_alipay_dict'):
                params['rnd_benefit_rules'] = self.rnd_benefit_rules.to_alipay_dict()
            else:
                params['rnd_benefit_rules'] = self.rnd_benefit_rules
        if self.rounding_mode:
            if hasattr(self.rounding_mode, 'to_alipay_dict'):
                params['rounding_mode'] = self.rounding_mode.to_alipay_dict()
            else:
                params['rounding_mode'] = self.rounding_mode
        if self.specified_amount:
            if hasattr(self.specified_amount, 'to_alipay_dict'):
                params['specified_amount'] = self.specified_amount.to_alipay_dict()
            else:
                params['specified_amount'] = self.specified_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VcpCalcFormula()
        if 'base_count' in d:
            o.base_count = d['base_count']
        if 'max_count' in d:
            o.max_count = d['max_count']
        if 'reduction_amount' in d:
            o.reduction_amount = d['reduction_amount']
        if 'reduction_ratio' in d:
            o.reduction_ratio = d['reduction_ratio']
        if 'rnd_benefit_rules' in d:
            o.rnd_benefit_rules = d['rnd_benefit_rules']
        if 'rounding_mode' in d:
            o.rounding_mode = d['rounding_mode']
        if 'specified_amount' in d:
            o.specified_amount = d['specified_amount']
        return o


