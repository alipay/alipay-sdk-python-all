#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCampaignRuleTagCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignRuleTagCreateResponse, self).__init__()
        self._customertag = None

    @property
    def customertag(self):
        return self._customertag

    @customertag.setter
    def customertag(self, value):
        self._customertag = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignRuleTagCreateResponse, self).parse_response_content(response_content)
        if 'customertag' in response:
            self.customertag = response['customertag']
