#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EnterpriseOpenRuleInfo import EnterpriseOpenRuleInfo


class AlipayEbppInvoiceEnterpriseconsumeEnterpriseopenruleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceEnterpriseconsumeEnterpriseopenruleQueryResponse, self).__init__()
        self._enterprise_open_rule_info = None

    @property
    def enterprise_open_rule_info(self):
        return self._enterprise_open_rule_info

    @enterprise_open_rule_info.setter
    def enterprise_open_rule_info(self, value):
        if isinstance(value, EnterpriseOpenRuleInfo):
            self._enterprise_open_rule_info = value
        else:
            self._enterprise_open_rule_info = EnterpriseOpenRuleInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceEnterpriseconsumeEnterpriseopenruleQueryResponse, self).parse_response_content(response_content)
        if 'enterprise_open_rule_info' in response:
            self.enterprise_open_rule_info = response['enterprise_open_rule_info']
