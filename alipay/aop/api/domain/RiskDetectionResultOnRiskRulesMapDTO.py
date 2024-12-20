#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RiskDetectionResultOnRuleDTO import RiskDetectionResultOnRuleDTO


class RiskDetectionResultOnRiskRulesMapDTO(object):

    def __init__(self):
        self._group_key = None
        self._risk_detection_result_on_rule_dto_list = None

    @property
    def group_key(self):
        return self._group_key

    @group_key.setter
    def group_key(self, value):
        self._group_key = value
    @property
    def risk_detection_result_on_rule_dto_list(self):
        return self._risk_detection_result_on_rule_dto_list

    @risk_detection_result_on_rule_dto_list.setter
    def risk_detection_result_on_rule_dto_list(self, value):
        if isinstance(value, list):
            self._risk_detection_result_on_rule_dto_list = list()
            for i in value:
                if isinstance(i, RiskDetectionResultOnRuleDTO):
                    self._risk_detection_result_on_rule_dto_list.append(i)
                else:
                    self._risk_detection_result_on_rule_dto_list.append(RiskDetectionResultOnRuleDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.group_key:
            if hasattr(self.group_key, 'to_alipay_dict'):
                params['group_key'] = self.group_key.to_alipay_dict()
            else:
                params['group_key'] = self.group_key
        if self.risk_detection_result_on_rule_dto_list:
            if isinstance(self.risk_detection_result_on_rule_dto_list, list):
                for i in range(0, len(self.risk_detection_result_on_rule_dto_list)):
                    element = self.risk_detection_result_on_rule_dto_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.risk_detection_result_on_rule_dto_list[i] = element.to_alipay_dict()
            if hasattr(self.risk_detection_result_on_rule_dto_list, 'to_alipay_dict'):
                params['risk_detection_result_on_rule_dto_list'] = self.risk_detection_result_on_rule_dto_list.to_alipay_dict()
            else:
                params['risk_detection_result_on_rule_dto_list'] = self.risk_detection_result_on_rule_dto_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RiskDetectionResultOnRiskRulesMapDTO()
        if 'group_key' in d:
            o.group_key = d['group_key']
        if 'risk_detection_result_on_rule_dto_list' in d:
            o.risk_detection_result_on_rule_dto_list = d['risk_detection_result_on_rule_dto_list']
        return o


