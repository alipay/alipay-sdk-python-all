#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MStepCashRule import MStepCashRule


class MEquityWorthInfo(object):

    def __init__(self):
        self._calculate_type = None
        self._cash_amount = None
        self._dynamic_rule_type = None
        self._max_discount_amount = None
        self._max_discount_count = None
        self._multi_step_cash_rules = None
        self._rate = None
        self._reduce_to_amount = None
        self._rounding_type = None
        self._type = None

    @property
    def calculate_type(self):
        return self._calculate_type

    @calculate_type.setter
    def calculate_type(self, value):
        self._calculate_type = value
    @property
    def cash_amount(self):
        return self._cash_amount

    @cash_amount.setter
    def cash_amount(self, value):
        self._cash_amount = value
    @property
    def dynamic_rule_type(self):
        return self._dynamic_rule_type

    @dynamic_rule_type.setter
    def dynamic_rule_type(self, value):
        self._dynamic_rule_type = value
    @property
    def max_discount_amount(self):
        return self._max_discount_amount

    @max_discount_amount.setter
    def max_discount_amount(self, value):
        self._max_discount_amount = value
    @property
    def max_discount_count(self):
        return self._max_discount_count

    @max_discount_count.setter
    def max_discount_count(self, value):
        self._max_discount_count = value
    @property
    def multi_step_cash_rules(self):
        return self._multi_step_cash_rules

    @multi_step_cash_rules.setter
    def multi_step_cash_rules(self, value):
        if isinstance(value, list):
            self._multi_step_cash_rules = list()
            for i in value:
                if isinstance(i, MStepCashRule):
                    self._multi_step_cash_rules.append(i)
                else:
                    self._multi_step_cash_rules.append(MStepCashRule.from_alipay_dict(i))
    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        self._rate = value
    @property
    def reduce_to_amount(self):
        return self._reduce_to_amount

    @reduce_to_amount.setter
    def reduce_to_amount(self, value):
        self._reduce_to_amount = value
    @property
    def rounding_type(self):
        return self._rounding_type

    @rounding_type.setter
    def rounding_type(self, value):
        self._rounding_type = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.calculate_type:
            if hasattr(self.calculate_type, 'to_alipay_dict'):
                params['calculate_type'] = self.calculate_type.to_alipay_dict()
            else:
                params['calculate_type'] = self.calculate_type
        if self.cash_amount:
            if hasattr(self.cash_amount, 'to_alipay_dict'):
                params['cash_amount'] = self.cash_amount.to_alipay_dict()
            else:
                params['cash_amount'] = self.cash_amount
        if self.dynamic_rule_type:
            if hasattr(self.dynamic_rule_type, 'to_alipay_dict'):
                params['dynamic_rule_type'] = self.dynamic_rule_type.to_alipay_dict()
            else:
                params['dynamic_rule_type'] = self.dynamic_rule_type
        if self.max_discount_amount:
            if hasattr(self.max_discount_amount, 'to_alipay_dict'):
                params['max_discount_amount'] = self.max_discount_amount.to_alipay_dict()
            else:
                params['max_discount_amount'] = self.max_discount_amount
        if self.max_discount_count:
            if hasattr(self.max_discount_count, 'to_alipay_dict'):
                params['max_discount_count'] = self.max_discount_count.to_alipay_dict()
            else:
                params['max_discount_count'] = self.max_discount_count
        if self.multi_step_cash_rules:
            if isinstance(self.multi_step_cash_rules, list):
                for i in range(0, len(self.multi_step_cash_rules)):
                    element = self.multi_step_cash_rules[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.multi_step_cash_rules[i] = element.to_alipay_dict()
            if hasattr(self.multi_step_cash_rules, 'to_alipay_dict'):
                params['multi_step_cash_rules'] = self.multi_step_cash_rules.to_alipay_dict()
            else:
                params['multi_step_cash_rules'] = self.multi_step_cash_rules
        if self.rate:
            if hasattr(self.rate, 'to_alipay_dict'):
                params['rate'] = self.rate.to_alipay_dict()
            else:
                params['rate'] = self.rate
        if self.reduce_to_amount:
            if hasattr(self.reduce_to_amount, 'to_alipay_dict'):
                params['reduce_to_amount'] = self.reduce_to_amount.to_alipay_dict()
            else:
                params['reduce_to_amount'] = self.reduce_to_amount
        if self.rounding_type:
            if hasattr(self.rounding_type, 'to_alipay_dict'):
                params['rounding_type'] = self.rounding_type.to_alipay_dict()
            else:
                params['rounding_type'] = self.rounding_type
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MEquityWorthInfo()
        if 'calculate_type' in d:
            o.calculate_type = d['calculate_type']
        if 'cash_amount' in d:
            o.cash_amount = d['cash_amount']
        if 'dynamic_rule_type' in d:
            o.dynamic_rule_type = d['dynamic_rule_type']
        if 'max_discount_amount' in d:
            o.max_discount_amount = d['max_discount_amount']
        if 'max_discount_count' in d:
            o.max_discount_count = d['max_discount_count']
        if 'multi_step_cash_rules' in d:
            o.multi_step_cash_rules = d['multi_step_cash_rules']
        if 'rate' in d:
            o.rate = d['rate']
        if 'reduce_to_amount' in d:
            o.reduce_to_amount = d['reduce_to_amount']
        if 'rounding_type' in d:
            o.rounding_type = d['rounding_type']
        if 'type' in d:
            o.type = d['type']
        return o


