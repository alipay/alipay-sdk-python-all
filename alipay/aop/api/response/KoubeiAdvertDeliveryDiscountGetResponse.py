#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DiscountInfo import DiscountInfo


class KoubeiAdvertDeliveryDiscountGetResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiAdvertDeliveryDiscountGetResponse, self).__init__()
        self._discounts = None
        self._recommend_id = None

    @property
    def discounts(self):
        return self._discounts

    @discounts.setter
    def discounts(self, value):
        if isinstance(value, DiscountInfo):
            self._discounts = value
        else:
            self._discounts = DiscountInfo.from_alipay_dict(value)
    @property
    def recommend_id(self):
        return self._recommend_id

    @recommend_id.setter
    def recommend_id(self, value):
        self._recommend_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiAdvertDeliveryDiscountGetResponse, self).parse_response_content(response_content)
        if 'discounts' in response:
            self.discounts = response['discounts']
        if 'recommend_id' in response:
            self.recommend_id = response['recommend_id']
