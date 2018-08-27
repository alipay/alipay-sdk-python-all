#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCdpRecommendQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCdpRecommendQueryResponse, self).__init__()
        self._recommend_id = None
        self._shop_info = None

    @property
    def recommend_id(self):
        return self._recommend_id

    @recommend_id.setter
    def recommend_id(self, value):
        self._recommend_id = value
    @property
    def shop_info(self):
        return self._shop_info

    @shop_info.setter
    def shop_info(self, value):
        self._shop_info = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCdpRecommendQueryResponse, self).parse_response_content(response_content)
        if 'recommend_id' in response:
            self.recommend_id = response['recommend_id']
        if 'shop_info' in response:
            self.shop_info = response['shop_info']
