#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AssetProduceItem import AssetProduceItem


class AntMerchantExpandAssetproduceAssignQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandAssetproduceAssignQueryResponse, self).__init__()
        self._asset_produce_items = None
        self._has_next_page = None

    @property
    def asset_produce_items(self):
        return self._asset_produce_items

    @asset_produce_items.setter
    def asset_produce_items(self, value):
        if isinstance(value, list):
            self._asset_produce_items = list()
            for i in value:
                if isinstance(i, AssetProduceItem):
                    self._asset_produce_items.append(i)
                else:
                    self._asset_produce_items.append(AssetProduceItem.from_alipay_dict(i))
    @property
    def has_next_page(self):
        return self._has_next_page

    @has_next_page.setter
    def has_next_page(self, value):
        self._has_next_page = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandAssetproduceAssignQueryResponse, self).parse_response_content(response_content)
        if 'asset_produce_items' in response:
            self.asset_produce_items = response['asset_produce_items']
        if 'has_next_page' in response:
            self.has_next_page = response['has_next_page']
