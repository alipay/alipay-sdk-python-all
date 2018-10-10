#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AssetReverseItem import AssetReverseItem


class AntMerchantExpandAssetreverseAssignQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandAssetreverseAssignQueryResponse, self).__init__()
        self._asset_reverse_items = None
        self._has_next_page = None

    @property
    def asset_reverse_items(self):
        return self._asset_reverse_items

    @asset_reverse_items.setter
    def asset_reverse_items(self, value):
        if isinstance(value, list):
            self._asset_reverse_items = list()
            for i in value:
                if isinstance(i, AssetReverseItem):
                    self._asset_reverse_items.append(i)
                else:
                    self._asset_reverse_items.append(AssetReverseItem.from_alipay_dict(i))
    @property
    def has_next_page(self):
        return self._has_next_page

    @has_next_page.setter
    def has_next_page(self, value):
        self._has_next_page = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandAssetreverseAssignQueryResponse, self).parse_response_content(response_content)
        if 'asset_reverse_items' in response:
            self.asset_reverse_items = response['asset_reverse_items']
        if 'has_next_page' in response:
            self.has_next_page = response['has_next_page']
