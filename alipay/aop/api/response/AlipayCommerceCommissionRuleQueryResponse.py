#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CommissionRuleDTO import CommissionRuleDTO
from alipay.aop.api.domain.CommissionRuleDTO import CommissionRuleDTO


class AlipayCommerceCommissionRuleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCommissionRuleQueryResponse, self).__init__()
        self._active_rule = None
        self._init_rule = None

    @property
    def active_rule(self):
        return self._active_rule

    @active_rule.setter
    def active_rule(self, value):
        if isinstance(value, CommissionRuleDTO):
            self._active_rule = value
        else:
            self._active_rule = CommissionRuleDTO.from_alipay_dict(value)
    @property
    def init_rule(self):
        return self._init_rule

    @init_rule.setter
    def init_rule(self, value):
        if isinstance(value, CommissionRuleDTO):
            self._init_rule = value
        else:
            self._init_rule = CommissionRuleDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCommissionRuleQueryResponse, self).parse_response_content(response_content)
        if 'active_rule' in response:
            self.active_rule = response['active_rule']
        if 'init_rule' in response:
            self.init_rule = response['init_rule']
