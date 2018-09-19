#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IntelligentPromoShopSummaryInfo import IntelligentPromoShopSummaryInfo


class KoubeiMarketingCampaignIntelligentShopConsultResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingCampaignIntelligentShopConsultResponse, self).__init__()
        self._items = None
        self._shops = None

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value
    @property
    def shops(self):
        return self._shops

    @shops.setter
    def shops(self, value):
        if isinstance(value, list):
            self._shops = list()
            for i in value:
                if isinstance(i, IntelligentPromoShopSummaryInfo):
                    self._shops.append(i)
                else:
                    self._shops.append(IntelligentPromoShopSummaryInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingCampaignIntelligentShopConsultResponse, self).parse_response_content(response_content)
        if 'items' in response:
            self.items = response['items']
        if 'shops' in response:
            self.shops = response['shops']
