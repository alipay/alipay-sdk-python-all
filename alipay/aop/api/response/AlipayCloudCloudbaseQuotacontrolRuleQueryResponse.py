#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.QuotaControlRule import QuotaControlRule


class AlipayCloudCloudbaseQuotacontrolRuleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseQuotacontrolRuleQueryResponse, self).__init__()
        self._rules = None

    @property
    def rules(self):
        return self._rules

    @rules.setter
    def rules(self, value):
        if isinstance(value, list):
            self._rules = list()
            for i in value:
                if isinstance(i, QuotaControlRule):
                    self._rules.append(i)
                else:
                    self._rules.append(QuotaControlRule.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseQuotacontrolRuleQueryResponse, self).parse_response_content(response_content)
        if 'rules' in response:
            self.rules = response['rules']
