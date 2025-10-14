#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MarketingPromotionOrderInfo import MarketingPromotionOrderInfo


class AlipayCommerceRecycleMarketingOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRecycleMarketingOrderQueryResponse, self).__init__()
        self._promotion_order_info = None

    @property
    def promotion_order_info(self):
        return self._promotion_order_info

    @promotion_order_info.setter
    def promotion_order_info(self, value):
        if isinstance(value, MarketingPromotionOrderInfo):
            self._promotion_order_info = value
        else:
            self._promotion_order_info = MarketingPromotionOrderInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRecycleMarketingOrderQueryResponse, self).parse_response_content(response_content)
        if 'promotion_order_info' in response:
            self.promotion_order_info = response['promotion_order_info']
