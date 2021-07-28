#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MarketActivityInfo import MarketActivityInfo


class AlipayMarketingCampaignPromotionactivityConsumerviewBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignPromotionactivityConsumerviewBatchqueryResponse, self).__init__()
        self._activities = None

    @property
    def activities(self):
        return self._activities

    @activities.setter
    def activities(self, value):
        if isinstance(value, list):
            self._activities = list()
            for i in value:
                if isinstance(i, MarketActivityInfo):
                    self._activities.append(i)
                else:
                    self._activities.append(MarketActivityInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignPromotionactivityConsumerviewBatchqueryResponse, self).parse_response_content(response_content)
        if 'activities' in response:
            self.activities = response['activities']
