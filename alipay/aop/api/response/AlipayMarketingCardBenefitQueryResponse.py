#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.McardTemplateBenefitQuery import McardTemplateBenefitQuery


class AlipayMarketingCardBenefitQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCardBenefitQueryResponse, self).__init__()
        self._mcard_template_benefit_query = None

    @property
    def mcard_template_benefit_query(self):
        return self._mcard_template_benefit_query

    @mcard_template_benefit_query.setter
    def mcard_template_benefit_query(self, value):
        if isinstance(value, list):
            self._mcard_template_benefit_query = list()
            for i in value:
                if isinstance(i, McardTemplateBenefitQuery):
                    self._mcard_template_benefit_query.append(i)
                else:
                    self._mcard_template_benefit_query.append(McardTemplateBenefitQuery.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCardBenefitQueryResponse, self).parse_response_content(response_content)
        if 'mcard_template_benefit_query' in response:
            self.mcard_template_benefit_query = response['mcard_template_benefit_query']
