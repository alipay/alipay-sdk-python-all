#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCampaignRuleCrowdCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignRuleCrowdCreateResponse, self).__init__()
        self._ruleid = None

    @property
    def ruleid(self):
        return self._ruleid

    @ruleid.setter
    def ruleid(self, value):
        self._ruleid = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignRuleCrowdCreateResponse, self).parse_response_content(response_content)
        if 'ruleid' in response:
            self.ruleid = response['ruleid']
