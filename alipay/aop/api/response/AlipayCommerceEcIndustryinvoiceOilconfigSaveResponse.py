#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CompanyRefinedOilRuleItem import CompanyRefinedOilRuleItem


class AlipayCommerceEcIndustryinvoiceOilconfigSaveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcIndustryinvoiceOilconfigSaveResponse, self).__init__()
        self._rule_list = None

    @property
    def rule_list(self):
        return self._rule_list

    @rule_list.setter
    def rule_list(self, value):
        if isinstance(value, list):
            self._rule_list = list()
            for i in value:
                if isinstance(i, CompanyRefinedOilRuleItem):
                    self._rule_list.append(i)
                else:
                    self._rule_list.append(CompanyRefinedOilRuleItem.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcIndustryinvoiceOilconfigSaveResponse, self).parse_response_content(response_content)
        if 'rule_list' in response:
            self.rule_list = response['rule_list']
