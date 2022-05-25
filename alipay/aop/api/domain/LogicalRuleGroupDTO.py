#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LogicalRuleItemDTO import LogicalRuleItemDTO


class LogicalRuleGroupDTO(object):

    def __init__(self):
        self._logical_rules = None

    @property
    def logical_rules(self):
        return self._logical_rules

    @logical_rules.setter
    def logical_rules(self, value):
        if isinstance(value, list):
            self._logical_rules = list()
            for i in value:
                if isinstance(i, LogicalRuleItemDTO):
                    self._logical_rules.append(i)
                else:
                    self._logical_rules.append(LogicalRuleItemDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.logical_rules:
            if isinstance(self.logical_rules, list):
                for i in range(0, len(self.logical_rules)):
                    element = self.logical_rules[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.logical_rules[i] = element.to_alipay_dict()
            if hasattr(self.logical_rules, 'to_alipay_dict'):
                params['logical_rules'] = self.logical_rules.to_alipay_dict()
            else:
                params['logical_rules'] = self.logical_rules
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LogicalRuleGroupDTO()
        if 'logical_rules' in d:
            o.logical_rules = d['logical_rules']
        return o


