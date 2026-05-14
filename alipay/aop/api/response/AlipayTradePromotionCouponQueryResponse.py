#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PromotionCoupon import PromotionCoupon


class AlipayTradePromotionCouponQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradePromotionCouponQueryResponse, self).__init__()
        self._coupon_list = None

    @property
    def coupon_list(self):
        return self._coupon_list

    @coupon_list.setter
    def coupon_list(self, value):
        if isinstance(value, list):
            self._coupon_list = list()
            for i in value:
                if isinstance(i, PromotionCoupon):
                    self._coupon_list.append(i)
                else:
                    self._coupon_list.append(PromotionCoupon.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayTradePromotionCouponQueryResponse, self).parse_response_content(response_content)
        if 'coupon_list' in response:
            self.coupon_list = response['coupon_list']
