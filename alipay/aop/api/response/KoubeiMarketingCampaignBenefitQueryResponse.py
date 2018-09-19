#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BenefitQueryInfo import BenefitQueryInfo


class KoubeiMarketingCampaignBenefitQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingCampaignBenefitQueryResponse, self).__init__()
        self._benefit_query_info = None

    @property
    def benefit_query_info(self):
        return self._benefit_query_info

    @benefit_query_info.setter
    def benefit_query_info(self, value):
        if isinstance(value, BenefitQueryInfo):
            self._benefit_query_info = value
        else:
            self._benefit_query_info = BenefitQueryInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingCampaignBenefitQueryResponse, self).parse_response_content(response_content)
        if 'benefit_query_info' in response:
            self.benefit_query_info = response['benefit_query_info']
