#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCampaignPrizepoolPrizeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignPrizepoolPrizeCreateResponse, self).__init__()
        self._prize_id = None

    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignPrizepoolPrizeCreateResponse, self).parse_response_content(response_content)
        if 'prize_id' in response:
            self.prize_id = response['prize_id']
