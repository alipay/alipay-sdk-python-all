#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsMktCampaignDTO import InsMktCampaignDTO


class AlipayInsMarketingCampaignQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsMarketingCampaignQueryResponse, self).__init__()
        self._mkt_campaign = None

    @property
    def mkt_campaign(self):
        return self._mkt_campaign

    @mkt_campaign.setter
    def mkt_campaign(self, value):
        if isinstance(value, InsMktCampaignDTO):
            self._mkt_campaign = value
        else:
            self._mkt_campaign = InsMktCampaignDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayInsMarketingCampaignQueryResponse, self).parse_response_content(response_content)
        if 'mkt_campaign' in response:
            self.mkt_campaign = response['mkt_campaign']
