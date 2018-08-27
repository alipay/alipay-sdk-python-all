#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsMktPreUseCampaignDTO import InsMktPreUseCampaignDTO
from alipay.aop.api.domain.InsMktPreUseCouponDTO import InsMktPreUseCouponDTO


class AlipayInsMarketingDiscountPreuseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsMarketingDiscountPreuseResponse, self).__init__()
        self._pre_use_campaigns = None
        self._pre_use_coupons = None

    @property
    def pre_use_campaigns(self):
        return self._pre_use_campaigns

    @pre_use_campaigns.setter
    def pre_use_campaigns(self, value):
        if isinstance(value, list):
            self._pre_use_campaigns = list()
            for i in value:
                if isinstance(i, InsMktPreUseCampaignDTO):
                    self._pre_use_campaigns.append(i)
                else:
                    self._pre_use_campaigns.append(InsMktPreUseCampaignDTO.from_alipay_dict(i))
    @property
    def pre_use_coupons(self):
        return self._pre_use_coupons

    @pre_use_coupons.setter
    def pre_use_coupons(self, value):
        if isinstance(value, list):
            self._pre_use_coupons = list()
            for i in value:
                if isinstance(i, InsMktPreUseCouponDTO):
                    self._pre_use_coupons.append(i)
                else:
                    self._pre_use_coupons.append(InsMktPreUseCouponDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayInsMarketingDiscountPreuseResponse, self).parse_response_content(response_content)
        if 'pre_use_campaigns' in response:
            self.pre_use_campaigns = response['pre_use_campaigns']
        if 'pre_use_coupons' in response:
            self.pre_use_coupons = response['pre_use_coupons']
