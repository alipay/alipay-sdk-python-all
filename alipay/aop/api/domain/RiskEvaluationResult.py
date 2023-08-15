#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RiskRuleResultDTO import RiskRuleResultDTO


class RiskEvaluationResult(object):

    def __init__(self):
        self._risk_instance_id = None
        self._risk_level = None
        self._risk_rule_result_list = None

    @property
    def risk_instance_id(self):
        return self._risk_instance_id

    @risk_instance_id.setter
    def risk_instance_id(self, value):
        self._risk_instance_id = value
    @property
    def risk_level(self):
        return self._risk_level

    @risk_level.setter
    def risk_level(self, value):
        self._risk_level = value
    @property
    def risk_rule_result_list(self):
        return self._risk_rule_result_list

    @risk_rule_result_list.setter
    def risk_rule_result_list(self, value):
        if isinstance(value, list):
            self._risk_rule_result_list = list()
            for i in value:
                if isinstance(i, RiskRuleResultDTO):
                    self._risk_rule_result_list.append(i)
                else:
                    self._risk_rule_result_list.append(RiskRuleResultDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.risk_instance_id:
            if hasattr(self.risk_instance_id, 'to_alipay_dict'):
                params['risk_instance_id'] = self.risk_instance_id.to_alipay_dict()
            else:
                params['risk_instance_id'] = self.risk_instance_id
        if self.risk_level:
            if hasattr(self.risk_level, 'to_alipay_dict'):
                params['risk_level'] = self.risk_level.to_alipay_dict()
            else:
                params['risk_level'] = self.risk_level
        if self.risk_rule_result_list:
            if isinstance(self.risk_rule_result_list, list):
                for i in range(0, len(self.risk_rule_result_list)):
                    element = self.risk_rule_result_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.risk_rule_result_list[i] = element.to_alipay_dict()
            if hasattr(self.risk_rule_result_list, 'to_alipay_dict'):
                params['risk_rule_result_list'] = self.risk_rule_result_list.to_alipay_dict()
            else:
                params['risk_rule_result_list'] = self.risk_rule_result_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RiskEvaluationResult()
        if 'risk_instance_id' in d:
            o.risk_instance_id = d['risk_instance_id']
        if 'risk_level' in d:
            o.risk_level = d['risk_level']
        if 'risk_rule_result_list' in d:
            o.risk_rule_result_list = d['risk_rule_result_list']
        return o


