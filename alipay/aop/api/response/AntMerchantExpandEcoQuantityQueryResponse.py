#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AssetEcoOrderQuantity import AssetEcoOrderQuantity


class AntMerchantExpandEcoQuantityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandEcoQuantityQueryResponse, self).__init__()
        self._eco_order_quantity = None

    @property
    def eco_order_quantity(self):
        return self._eco_order_quantity

    @eco_order_quantity.setter
    def eco_order_quantity(self, value):
        if isinstance(value, list):
            self._eco_order_quantity = list()
            for i in value:
                if isinstance(i, AssetEcoOrderQuantity):
                    self._eco_order_quantity.append(i)
                else:
                    self._eco_order_quantity.append(AssetEcoOrderQuantity.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandEcoQuantityQueryResponse, self).parse_response_content(response_content)
        if 'eco_order_quantity' in response:
            self.eco_order_quantity = response['eco_order_quantity']
