#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMarketingCampaignCrowdCountResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingCampaignCrowdCountResponse, self).__init__()
        self._dimension_values = None
        self._summary_values = None

    @property
    def dimension_values(self):
        return self._dimension_values

    @dimension_values.setter
    def dimension_values(self, value):
        self._dimension_values = value
    @property
    def summary_values(self):
        return self._summary_values

    @summary_values.setter
    def summary_values(self, value):
        self._summary_values = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingCampaignCrowdCountResponse, self).parse_response_content(response_content)
        if 'dimension_values' in response:
            self.dimension_values = response['dimension_values']
        if 'summary_values' in response:
            self.summary_values = response['summary_values']
