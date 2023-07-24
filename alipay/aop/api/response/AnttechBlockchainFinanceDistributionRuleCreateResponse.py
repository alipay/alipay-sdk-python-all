#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainFinanceDistributionRuleCreateResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceDistributionRuleCreateResponse, self).__init__()
        self._distribution_rule_id = None
        self._status = None

    @property
    def distribution_rule_id(self):
        return self._distribution_rule_id

    @distribution_rule_id.setter
    def distribution_rule_id(self, value):
        self._distribution_rule_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceDistributionRuleCreateResponse, self).parse_response_content(response_content)
        if 'distribution_rule_id' in response:
            self.distribution_rule_id = response['distribution_rule_id']
        if 'status' in response:
            self.status = response['status']
