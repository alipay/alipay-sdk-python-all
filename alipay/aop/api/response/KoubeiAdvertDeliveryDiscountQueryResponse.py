#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DiscountInfo import DiscountInfo


class KoubeiAdvertDeliveryDiscountQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiAdvertDeliveryDiscountQueryResponse, self).__init__()
        self._discount = None

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, DiscountInfo):
            self._discount = value
        else:
            self._discount = DiscountInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiAdvertDeliveryDiscountQueryResponse, self).parse_response_content(response_content)
        if 'discount' in response:
            self.discount = response['discount']
