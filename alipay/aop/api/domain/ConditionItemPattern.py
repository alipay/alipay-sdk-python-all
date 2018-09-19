#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConditionItemPattern(object):

    def __init__(self):
        self._logical_operator = None
        self._operation_value = None
        self._operator_rule = None
        self._period = None
        self._rule_unit = None

    @property
    def logical_operator(self):
        return self._logical_operator

    @logical_operator.setter
    def logical_operator(self, value):
        self._logical_operator = value
    @property
    def operation_value(self):
        return self._operation_value

    @operation_value.setter
    def operation_value(self, value):
        self._operation_value = value
    @property
    def operator_rule(self):
        return self._operator_rule

    @operator_rule.setter
    def operator_rule(self, value):
        self._operator_rule = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def rule_unit(self):
        return self._rule_unit

    @rule_unit.setter
    def rule_unit(self, value):
        self._rule_unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.logical_operator:
            if hasattr(self.logical_operator, 'to_alipay_dict'):
                params['logical_operator'] = self.logical_operator.to_alipay_dict()
            else:
                params['logical_operator'] = self.logical_operator
        if self.operation_value:
            if hasattr(self.operation_value, 'to_alipay_dict'):
                params['operation_value'] = self.operation_value.to_alipay_dict()
            else:
                params['operation_value'] = self.operation_value
        if self.operator_rule:
            if hasattr(self.operator_rule, 'to_alipay_dict'):
                params['operator_rule'] = self.operator_rule.to_alipay_dict()
            else:
                params['operator_rule'] = self.operator_rule
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.rule_unit:
            if hasattr(self.rule_unit, 'to_alipay_dict'):
                params['rule_unit'] = self.rule_unit.to_alipay_dict()
            else:
                params['rule_unit'] = self.rule_unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConditionItemPattern()
        if 'logical_operator' in d:
            o.logical_operator = d['logical_operator']
        if 'operation_value' in d:
            o.operation_value = d['operation_value']
        if 'operator_rule' in d:
            o.operator_rule = d['operator_rule']
        if 'period' in d:
            o.period = d['period']
        if 'rule_unit' in d:
            o.rule_unit = d['rule_unit']
        return o


