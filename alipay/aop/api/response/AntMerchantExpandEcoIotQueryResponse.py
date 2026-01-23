#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AssetEcoIotOrderInfo import AssetEcoIotOrderInfo


class AntMerchantExpandEcoIotQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandEcoIotQueryResponse, self).__init__()
        self._eco_iot_orders = None
        self._has_next_page = None
        self._total_size = None

    @property
    def eco_iot_orders(self):
        return self._eco_iot_orders

    @eco_iot_orders.setter
    def eco_iot_orders(self, value):
        if isinstance(value, list):
            self._eco_iot_orders = list()
            for i in value:
                if isinstance(i, AssetEcoIotOrderInfo):
                    self._eco_iot_orders.append(i)
                else:
                    self._eco_iot_orders.append(AssetEcoIotOrderInfo.from_alipay_dict(i))
    @property
    def has_next_page(self):
        return self._has_next_page

    @has_next_page.setter
    def has_next_page(self, value):
        self._has_next_page = value
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandEcoIotQueryResponse, self).parse_response_content(response_content)
        if 'eco_iot_orders' in response:
            self.eco_iot_orders = response['eco_iot_orders']
        if 'has_next_page' in response:
            self.has_next_page = response['has_next_page']
        if 'total_size' in response:
            self.total_size = response['total_size']
