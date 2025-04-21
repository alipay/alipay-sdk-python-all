#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EduCheckInRule import EduCheckInRule


class AlipayCommerceEducateCheckinRuleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateCheckinRuleQueryResponse, self).__init__()
        self._rule_info = None

    @property
    def rule_info(self):
        return self._rule_info

    @rule_info.setter
    def rule_info(self, value):
        if isinstance(value, EduCheckInRule):
            self._rule_info = value
        else:
            self._rule_info = EduCheckInRule.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateCheckinRuleQueryResponse, self).parse_response_content(response_content)
        if 'rule_info' in response:
            self.rule_info = response['rule_info']
