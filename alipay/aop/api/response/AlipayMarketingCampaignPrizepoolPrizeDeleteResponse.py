#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCampaignPrizepoolPrizeDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignPrizepoolPrizeDeleteResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignPrizepoolPrizeDeleteResponse, self).parse_response_content(response_content)
