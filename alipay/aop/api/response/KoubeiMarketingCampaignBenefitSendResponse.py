#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMarketingCampaignBenefitSendResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingCampaignBenefitSendResponse, self).__init__()
        self._benefit_ids = None

    @property
    def benefit_ids(self):
        return self._benefit_ids

    @benefit_ids.setter
    def benefit_ids(self, value):
        if isinstance(value, list):
            self._benefit_ids = list()
            for i in value:
                self._benefit_ids.append(i)

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingCampaignBenefitSendResponse, self).parse_response_content(response_content)
        if 'benefit_ids' in response:
            self.benefit_ids = response['benefit_ids']
