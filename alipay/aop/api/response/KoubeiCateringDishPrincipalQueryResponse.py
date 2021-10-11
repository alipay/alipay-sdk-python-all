#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiCateringDishPrincipalQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringDishPrincipalQueryResponse, self).__init__()
        self._dish_id = None
        self._item_id = None
        self._item_sku_id = None
        self._sku_id = None

    @property
    def dish_id(self):
        return self._dish_id

    @dish_id.setter
    def dish_id(self, value):
        self._dish_id = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_sku_id(self):
        return self._item_sku_id

    @item_sku_id.setter
    def item_sku_id(self, value):
        self._item_sku_id = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringDishPrincipalQueryResponse, self).parse_response_content(response_content)
        if 'dish_id' in response:
            self.dish_id = response['dish_id']
        if 'item_id' in response:
            self.item_id = response['item_id']
        if 'item_sku_id' in response:
            self.item_sku_id = response['item_sku_id']
        if 'sku_id' in response:
            self.sku_id = response['sku_id']
