#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExpenseCtrRuleInfo(object):

    def __init__(self):
        self._rule_factor = None
        self._rule_id = None
        self._rule_name = None
        self._rule_operator = None
        self._rule_value = None

    @property
    def rule_factor(self):
        return self._rule_factor

    @rule_factor.setter
    def rule_factor(self, value):
        self._rule_factor = value
    @property
    def rule_id(self):
        return self._rule_id

    @rule_id.setter
    def rule_id(self, value):
        self._rule_id = value
    @property
    def rule_name(self):
        return self._rule_name

    @rule_name.setter
    def rule_name(self, value):
        self._rule_name = value
    @property
    def rule_operator(self):
        return self._rule_operator

    @rule_operator.setter
    def rule_operator(self, value):
        self._rule_operator = value
    @property
    def rule_value(self):
        return self._rule_value

    @rule_value.setter
    def rule_value(self, value):
        self._rule_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.rule_factor:
            if hasattr(self.rule_factor, 'to_alipay_dict'):
                params['rule_factor'] = self.rule_factor.to_alipay_dict()
            else:
                params['rule_factor'] = self.rule_factor
        if self.rule_id:
            if hasattr(self.rule_id, 'to_alipay_dict'):
                params['rule_id'] = self.rule_id.to_alipay_dict()
            else:
                params['rule_id'] = self.rule_id
        if self.rule_name:
            if hasattr(self.rule_name, 'to_alipay_dict'):
                params['rule_name'] = self.rule_name.to_alipay_dict()
            else:
                params['rule_name'] = self.rule_name
        if self.rule_operator:
            if hasattr(self.rule_operator, 'to_alipay_dict'):
                params['rule_operator'] = self.rule_operator.to_alipay_dict()
            else:
                params['rule_operator'] = self.rule_operator
        if self.rule_value:
            if hasattr(self.rule_value, 'to_alipay_dict'):
                params['rule_value'] = self.rule_value.to_alipay_dict()
            else:
                params['rule_value'] = self.rule_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExpenseCtrRuleInfo()
        if 'rule_factor' in d:
            o.rule_factor = d['rule_factor']
        if 'rule_id' in d:
            o.rule_id = d['rule_id']
        if 'rule_name' in d:
            o.rule_name = d['rule_name']
        if 'rule_operator' in d:
            o.rule_operator = d['rule_operator']
        if 'rule_value' in d:
            o.rule_value = d['rule_value']
        return o


