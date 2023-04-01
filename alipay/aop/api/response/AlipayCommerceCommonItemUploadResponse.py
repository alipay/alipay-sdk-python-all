#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IndustryItemSkuSyncResultDTO import IndustryItemSkuSyncResultDTO


class AlipayCommerceCommonItemUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCommonItemUploadResponse, self).__init__()
        self._item_id = None
        self._platform_item_id = None
        self._sku_result_list = None

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def platform_item_id(self):
        return self._platform_item_id

    @platform_item_id.setter
    def platform_item_id(self, value):
        self._platform_item_id = value
    @property
    def sku_result_list(self):
        return self._sku_result_list

    @sku_result_list.setter
    def sku_result_list(self, value):
        if isinstance(value, list):
            self._sku_result_list = list()
            for i in value:
                if isinstance(i, IndustryItemSkuSyncResultDTO):
                    self._sku_result_list.append(i)
                else:
                    self._sku_result_list.append(IndustryItemSkuSyncResultDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCommonItemUploadResponse, self).parse_response_content(response_content)
        if 'item_id' in response:
            self.item_id = response['item_id']
        if 'platform_item_id' in response:
            self.platform_item_id = response['platform_item_id']
        if 'sku_result_list' in response:
            self.sku_result_list = response['sku_result_list']
