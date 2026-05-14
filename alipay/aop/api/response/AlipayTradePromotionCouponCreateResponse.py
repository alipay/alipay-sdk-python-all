#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PromotionCoupon import PromotionCoupon


class AlipayTradePromotionCouponCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradePromotionCouponCreateResponse, self).__init__()
        self._coupon_info = None

    @property
    def coupon_info(self):
        return self._coupon_info

    @coupon_info.setter
    def coupon_info(self, value):
        if isinstance(value, PromotionCoupon):
            self._coupon_info = value
        else:
            self._coupon_info = PromotionCoupon.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayTradePromotionCouponCreateResponse, self).parse_response_content(response_content)
        if 'coupon_info' in response:
            self.coupon_info = response['coupon_info']
