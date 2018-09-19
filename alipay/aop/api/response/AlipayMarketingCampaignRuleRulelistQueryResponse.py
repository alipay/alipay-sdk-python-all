#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CrowdRuleInfo import CrowdRuleInfo


class AlipayMarketingCampaignRuleRulelistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignRuleRulelistQueryResponse, self).__init__()
        self._rulelist = None

    @property
    def rulelist(self):
        return self._rulelist

    @rulelist.setter
    def rulelist(self, value):
        if isinstance(value, list):
            self._rulelist = list()
            for i in value:
                if isinstance(i, CrowdRuleInfo):
                    self._rulelist.append(i)
                else:
                    self._rulelist.append(CrowdRuleInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignRuleRulelistQueryResponse, self).parse_response_content(response_content)
        if 'rulelist' in response:
            self.rulelist = response['rulelist']
