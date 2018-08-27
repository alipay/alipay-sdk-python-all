#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PromoItemInfo import PromoItemInfo


class KoubeiMarketingCampaignItemQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingCampaignItemQueryResponse, self).__init__()
        self._item = None

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, value):
        if isinstance(value, PromoItemInfo):
            self._item = value
        else:
            self._item = PromoItemInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingCampaignItemQueryResponse, self).parse_response_content(response_content)
        if 'item' in response:
            self.item = response['item']
