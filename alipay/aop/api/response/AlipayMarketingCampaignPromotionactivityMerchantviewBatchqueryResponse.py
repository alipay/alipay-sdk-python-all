#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MarketActivityInfo import MarketActivityInfo
from alipay.aop.api.domain.Paginator import Paginator


class AlipayMarketingCampaignPromotionactivityMerchantviewBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignPromotionactivityMerchantviewBatchqueryResponse, self).__init__()
        self._activities = None
        self._paginator = None

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
    @property
    def paginator(self):
        return self._paginator

    @paginator.setter
    def paginator(self, value):
        if isinstance(value, Paginator):
            self._paginator = value
        else:
            self._paginator = Paginator.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignPromotionactivityMerchantviewBatchqueryResponse, self).parse_response_content(response_content)
        if 'activities' in response:
            self.activities = response['activities']
        if 'paginator' in response:
            self.paginator = response['paginator']
