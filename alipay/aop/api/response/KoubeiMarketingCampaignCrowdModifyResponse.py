#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMarketingCampaignCrowdModifyResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingCampaignCrowdModifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingCampaignCrowdModifyResponse, self).parse_response_content(response_content)
