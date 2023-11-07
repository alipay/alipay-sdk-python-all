#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FeeItemPrice import FeeItemPrice


class AlipayCloudCloudbaseExtensionFeeGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseExtensionFeeGetResponse, self).__init__()
        self._fee_item_prices = None

    @property
    def fee_item_prices(self):
        return self._fee_item_prices

    @fee_item_prices.setter
    def fee_item_prices(self, value):
        if isinstance(value, list):
            self._fee_item_prices = list()
            for i in value:
                if isinstance(i, FeeItemPrice):
                    self._fee_item_prices.append(i)
                else:
                    self._fee_item_prices.append(FeeItemPrice.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseExtensionFeeGetResponse, self).parse_response_content(response_content)
        if 'fee_item_prices' in response:
            self.fee_item_prices = response['fee_item_prices']
