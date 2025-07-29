#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ItemSkuIdPair import ItemSkuIdPair


class AlipayOpenAppItemModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppItemModifyResponse, self).__init__()
        self._business_model = None
        self._item_id = None
        self._out_item_id = None
        self._skus = None

    @property
    def business_model(self):
        return self._business_model

    @business_model.setter
    def business_model(self, value):
        self._business_model = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value
    @property
    def skus(self):
        return self._skus

    @skus.setter
    def skus(self, value):
        if isinstance(value, list):
            self._skus = list()
            for i in value:
                if isinstance(i, ItemSkuIdPair):
                    self._skus.append(i)
                else:
                    self._skus.append(ItemSkuIdPair.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppItemModifyResponse, self).parse_response_content(response_content)
        if 'business_model' in response:
            self.business_model = response['business_model']
        if 'item_id' in response:
            self.item_id = response['item_id']
        if 'out_item_id' in response:
            self.out_item_id = response['out_item_id']
        if 'skus' in response:
            self.skus = response['skus']
