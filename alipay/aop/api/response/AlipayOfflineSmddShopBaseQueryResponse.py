#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AddressBean import AddressBean


class AlipayOfflineSmddShopBaseQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineSmddShopBaseQueryResponse, self).__init__()
        self._item_pic_show_type = None
        self._required_category = None
        self._required_item_type = None
        self._shop_address = None
        self._shop_id = None
        self._shop_name = None
        self._shop_notice = None

    @property
    def item_pic_show_type(self):
        return self._item_pic_show_type

    @item_pic_show_type.setter
    def item_pic_show_type(self, value):
        self._item_pic_show_type = value
    @property
    def required_category(self):
        return self._required_category

    @required_category.setter
    def required_category(self, value):
        self._required_category = value
    @property
    def required_item_type(self):
        return self._required_item_type

    @required_item_type.setter
    def required_item_type(self, value):
        self._required_item_type = value
    @property
    def shop_address(self):
        return self._shop_address

    @shop_address.setter
    def shop_address(self, value):
        if isinstance(value, AddressBean):
            self._shop_address = value
        else:
            self._shop_address = AddressBean.from_alipay_dict(value)
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_notice(self):
        return self._shop_notice

    @shop_notice.setter
    def shop_notice(self, value):
        self._shop_notice = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineSmddShopBaseQueryResponse, self).parse_response_content(response_content)
        if 'item_pic_show_type' in response:
            self.item_pic_show_type = response['item_pic_show_type']
        if 'required_category' in response:
            self.required_category = response['required_category']
        if 'required_item_type' in response:
            self.required_item_type = response['required_item_type']
        if 'shop_address' in response:
            self.shop_address = response['shop_address']
        if 'shop_id' in response:
            self.shop_id = response['shop_id']
        if 'shop_name' in response:
            self.shop_name = response['shop_name']
        if 'shop_notice' in response:
            self.shop_notice = response['shop_notice']
