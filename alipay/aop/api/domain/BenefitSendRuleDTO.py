#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BenefitBudgetDTO import BenefitBudgetDTO
from alipay.aop.api.domain.CollectLimitRuleDTO import CollectLimitRuleDTO


class BenefitSendRuleDTO(object):

    def __init__(self):
        self._budget = None
        self._collect_limit_rules = None

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, value):
        if isinstance(value, BenefitBudgetDTO):
            self._budget = value
        else:
            self._budget = BenefitBudgetDTO.from_alipay_dict(value)
    @property
    def collect_limit_rules(self):
        return self._collect_limit_rules

    @collect_limit_rules.setter
    def collect_limit_rules(self, value):
        if isinstance(value, list):
            self._collect_limit_rules = list()
            for i in value:
                if isinstance(i, CollectLimitRuleDTO):
                    self._collect_limit_rules.append(i)
                else:
                    self._collect_limit_rules.append(CollectLimitRuleDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.budget:
            if hasattr(self.budget, 'to_alipay_dict'):
                params['budget'] = self.budget.to_alipay_dict()
            else:
                params['budget'] = self.budget
        if self.collect_limit_rules:
            if isinstance(self.collect_limit_rules, list):
                for i in range(0, len(self.collect_limit_rules)):
                    element = self.collect_limit_rules[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.collect_limit_rules[i] = element.to_alipay_dict()
            if hasattr(self.collect_limit_rules, 'to_alipay_dict'):
                params['collect_limit_rules'] = self.collect_limit_rules.to_alipay_dict()
            else:
                params['collect_limit_rules'] = self.collect_limit_rules
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitSendRuleDTO()
        if 'budget' in d:
            o.budget = d['budget']
        if 'collect_limit_rules' in d:
            o.collect_limit_rules = d['collect_limit_rules']
        return o


