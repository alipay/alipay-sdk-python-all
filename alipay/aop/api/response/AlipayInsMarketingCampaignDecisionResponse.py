#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsMktCampaignDTO import InsMktCampaignDTO


class AlipayInsMarketingCampaignDecisionResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsMarketingCampaignDecisionResponse, self).__init__()
        self._mkt_campaigns = None

    @property
    def mkt_campaigns(self):
        return self._mkt_campaigns

    @mkt_campaigns.setter
    def mkt_campaigns(self, value):
        if isinstance(value, list):
            self._mkt_campaigns = list()
            for i in value:
                if isinstance(i, InsMktCampaignDTO):
                    self._mkt_campaigns.append(i)
                else:
                    self._mkt_campaigns.append(InsMktCampaignDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayInsMarketingCampaignDecisionResponse, self).parse_response_content(response_content)
        if 'mkt_campaigns' in response:
            self.mkt_campaigns = response['mkt_campaigns']
