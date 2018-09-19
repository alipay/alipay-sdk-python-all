#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RetailItemDescription import RetailItemDescription


class KoubeiRetailItemQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiRetailItemQueryResponse, self).__init__()
        self._cover = None
        self._descriptions = None
        self._discount_rate = None
        self._gmt_end = None
        self._gmt_start = None
        self._item_id = None
        self._item_status = None
        self._original_amount = None
        self._picture_list = None
        self._reduce_to_amount = None
        self._shop_list = None
        self._sku_list = None
        self._title = None
        self._type = None
        self._value_amount = None

    @property
    def cover(self):
        return self._cover

    @cover.setter
    def cover(self, value):
        self._cover = value
    @property
    def descriptions(self):
        return self._descriptions

    @descriptions.setter
    def descriptions(self, value):
        if isinstance(value, list):
            self._descriptions = list()
            for i in value:
                if isinstance(i, RetailItemDescription):
                    self._descriptions.append(i)
                else:
                    self._descriptions.append(RetailItemDescription.from_alipay_dict(i))
    @property
    def discount_rate(self):
        return self._discount_rate

    @discount_rate.setter
    def discount_rate(self, value):
        self._discount_rate = value
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def gmt_start(self):
        return self._gmt_start

    @gmt_start.setter
    def gmt_start(self, value):
        self._gmt_start = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_status(self):
        return self._item_status

    @item_status.setter
    def item_status(self, value):
        self._item_status = value
    @property
    def original_amount(self):
        return self._original_amount

    @original_amount.setter
    def original_amount(self, value):
        self._original_amount = value
    @property
    def picture_list(self):
        return self._picture_list

    @picture_list.setter
    def picture_list(self, value):
        if isinstance(value, list):
            self._picture_list = list()
            for i in value:
                self._picture_list.append(i)
    @property
    def reduce_to_amount(self):
        return self._reduce_to_amount

    @reduce_to_amount.setter
    def reduce_to_amount(self, value):
        self._reduce_to_amount = value
    @property
    def shop_list(self):
        return self._shop_list

    @shop_list.setter
    def shop_list(self, value):
        if isinstance(value, list):
            self._shop_list = list()
            for i in value:
                self._shop_list.append(i)
    @property
    def sku_list(self):
        return self._sku_list

    @sku_list.setter
    def sku_list(self, value):
        if isinstance(value, list):
            self._sku_list = list()
            for i in value:
                self._sku_list.append(i)
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def value_amount(self):
        return self._value_amount

    @value_amount.setter
    def value_amount(self, value):
        self._value_amount = value

    def parse_response_content(self, response_content):
        response = super(KoubeiRetailItemQueryResponse, self).parse_response_content(response_content)
        if 'cover' in response:
            self.cover = response['cover']
        if 'descriptions' in response:
            self.descriptions = response['descriptions']
        if 'discount_rate' in response:
            self.discount_rate = response['discount_rate']
        if 'gmt_end' in response:
            self.gmt_end = response['gmt_end']
        if 'gmt_start' in response:
            self.gmt_start = response['gmt_start']
        if 'item_id' in response:
            self.item_id = response['item_id']
        if 'item_status' in response:
            self.item_status = response['item_status']
        if 'original_amount' in response:
            self.original_amount = response['original_amount']
        if 'picture_list' in response:
            self.picture_list = response['picture_list']
        if 'reduce_to_amount' in response:
            self.reduce_to_amount = response['reduce_to_amount']
        if 'shop_list' in response:
            self.shop_list = response['shop_list']
        if 'sku_list' in response:
            self.sku_list = response['sku_list']
        if 'title' in response:
            self.title = response['title']
        if 'type' in response:
            self.type = response['type']
        if 'value_amount' in response:
            self.value_amount = response['value_amount']
