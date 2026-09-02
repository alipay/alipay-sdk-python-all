#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RuleCheckResult import RuleCheckResult


class AlipayCommerceMedicalRegisterRuleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalRegisterRuleQueryResponse, self).__init__()
        self._hit = None
        self._rule_check_res_list = None

    @property
    def hit(self):
        return self._hit

    @hit.setter
    def hit(self, value):
        self._hit = value
    @property
    def rule_check_res_list(self):
        return self._rule_check_res_list

    @rule_check_res_list.setter
    def rule_check_res_list(self, value):
        if isinstance(value, list):
            self._rule_check_res_list = list()
            for i in value:
                if isinstance(i, RuleCheckResult):
                    self._rule_check_res_list.append(i)
                else:
                    self._rule_check_res_list.append(RuleCheckResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalRegisterRuleQueryResponse, self).parse_response_content(response_content)
        if 'hit' in response:
            self.hit = response['hit']
        if 'rule_check_res_list' in response:
            self.rule_check_res_list = response['rule_check_res_list']
