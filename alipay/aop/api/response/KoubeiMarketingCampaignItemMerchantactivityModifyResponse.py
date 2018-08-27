#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMarketingCampaignItemMerchantactivityModifyResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingCampaignItemMerchantactivityModifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingCampaignItemMerchantactivityModifyResponse, self).parse_response_content(response_content)
