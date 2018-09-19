#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMarketingCampaignDetailInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingCampaignDetailInfoQueryResponse, self).__init__()
        self._limit_shops = None

    @property
    def limit_shops(self):
        return self._limit_shops

    @limit_shops.setter
    def limit_shops(self, value):
        self._limit_shops = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingCampaignDetailInfoQueryResponse, self).parse_response_content(response_content)
        if 'limit_shops' in response:
            self.limit_shops = response['limit_shops']
