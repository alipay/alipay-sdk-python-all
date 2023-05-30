#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RuleVO(object):

    def __init__(self):
        self._module_code = None
        self._rule_conditions = None

    @property
    def module_code(self):
        return self._module_code

    @module_code.setter
    def module_code(self, value):
        self._module_code = value
    @property
    def rule_conditions(self):
        return self._rule_conditions

    @rule_conditions.setter
    def rule_conditions(self, value):
        self._rule_conditions = value


    def to_alipay_dict(self):
        params = dict()
        if self.module_code:
            if hasattr(self.module_code, 'to_alipay_dict'):
                params['module_code'] = self.module_code.to_alipay_dict()
            else:
                params['module_code'] = self.module_code
        if self.rule_conditions:
            if hasattr(self.rule_conditions, 'to_alipay_dict'):
                params['rule_conditions'] = self.rule_conditions.to_alipay_dict()
            else:
                params['rule_conditions'] = self.rule_conditions
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RuleVO()
        if 'module_code' in d:
            o.module_code = d['module_code']
        if 'rule_conditions' in d:
            o.rule_conditions = d['rule_conditions']
        return o


