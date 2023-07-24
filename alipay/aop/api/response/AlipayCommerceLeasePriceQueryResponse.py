#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LeaseItemSkuDTO import LeaseItemSkuDTO


class AlipayCommerceLeasePriceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLeasePriceQueryResponse, self).__init__()
        self._item_id = None
        self._lowest_price = None
        self._lowest_price_sku_id = None
        self._skus = None

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def lowest_price(self):
        return self._lowest_price

    @lowest_price.setter
    def lowest_price(self, value):
        self._lowest_price = value
    @property
    def lowest_price_sku_id(self):
        return self._lowest_price_sku_id

    @lowest_price_sku_id.setter
    def lowest_price_sku_id(self, value):
        self._lowest_price_sku_id = value
    @property
    def skus(self):
        return self._skus

    @skus.setter
    def skus(self, value):
        if isinstance(value, list):
            self._skus = list()
            for i in value:
                if isinstance(i, LeaseItemSkuDTO):
                    self._skus.append(i)
                else:
                    self._skus.append(LeaseItemSkuDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLeasePriceQueryResponse, self).parse_response_content(response_content)
        if 'item_id' in response:
            self.item_id = response['item_id']
        if 'lowest_price' in response:
            self.lowest_price = response['lowest_price']
        if 'lowest_price_sku_id' in response:
            self.lowest_price_sku_id = response['lowest_price_sku_id']
        if 'skus' in response:
            self.skus = response['skus']
