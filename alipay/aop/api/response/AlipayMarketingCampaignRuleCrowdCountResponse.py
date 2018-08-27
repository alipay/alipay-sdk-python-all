#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCampaignRuleCrowdCountResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignRuleCrowdCountResponse, self).__init__()
        self._crowdcount = None

    @property
    def crowdcount(self):
        return self._crowdcount

    @crowdcount.setter
    def crowdcount(self, value):
        self._crowdcount = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignRuleCrowdCountResponse, self).parse_response_content(response_content)
        if 'crowdcount' in response:
            self.crowdcount = response['crowdcount']
