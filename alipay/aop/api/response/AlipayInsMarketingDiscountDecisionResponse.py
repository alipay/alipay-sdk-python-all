#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsMktCouponCampaignDTO import InsMktCouponCampaignDTO
from alipay.aop.api.domain.InsMktCouponDTO import InsMktCouponDTO


class AlipayInsMarketingDiscountDecisionResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsMarketingDiscountDecisionResponse, self).__init__()
        self._mkt_coupon_campaigns = None
        self._mkt_coupons = None

    @property
    def mkt_coupon_campaigns(self):
        return self._mkt_coupon_campaigns

    @mkt_coupon_campaigns.setter
    def mkt_coupon_campaigns(self, value):
        if isinstance(value, list):
            self._mkt_coupon_campaigns = list()
            for i in value:
                if isinstance(i, InsMktCouponCampaignDTO):
                    self._mkt_coupon_campaigns.append(i)
                else:
                    self._mkt_coupon_campaigns.append(InsMktCouponCampaignDTO.from_alipay_dict(i))
    @property
    def mkt_coupons(self):
        return self._mkt_coupons

    @mkt_coupons.setter
    def mkt_coupons(self, value):
        if isinstance(value, list):
            self._mkt_coupons = list()
            for i in value:
                if isinstance(i, InsMktCouponDTO):
                    self._mkt_coupons.append(i)
                else:
                    self._mkt_coupons.append(InsMktCouponDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayInsMarketingDiscountDecisionResponse, self).parse_response_content(response_content)
        if 'mkt_coupon_campaigns' in response:
            self.mkt_coupon_campaigns = response['mkt_coupon_campaigns']
        if 'mkt_coupons' in response:
            self.mkt_coupons = response['mkt_coupons']
