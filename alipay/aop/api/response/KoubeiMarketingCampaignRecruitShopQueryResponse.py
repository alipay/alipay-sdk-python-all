#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecruitShopInfo import RecruitShopInfo


class KoubeiMarketingCampaignRecruitShopQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingCampaignRecruitShopQueryResponse, self).__init__()
        self._plan_id = None
        self._shop_count = None
        self._shop_info = None

    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def shop_count(self):
        return self._shop_count

    @shop_count.setter
    def shop_count(self, value):
        self._shop_count = value
    @property
    def shop_info(self):
        return self._shop_info

    @shop_info.setter
    def shop_info(self, value):
        if isinstance(value, list):
            self._shop_info = list()
            for i in value:
                if isinstance(i, RecruitShopInfo):
                    self._shop_info.append(i)
                else:
                    self._shop_info.append(RecruitShopInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingCampaignRecruitShopQueryResponse, self).parse_response_content(response_content)
        if 'plan_id' in response:
            self.plan_id = response['plan_id']
        if 'shop_count' in response:
            self.shop_count = response['shop_count']
        if 'shop_info' in response:
            self.shop_info = response['shop_info']
