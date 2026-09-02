#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AShopItemVO import AShopItemVO


class AlipayOpenAppUnishopItemlistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppUnishopItemlistQueryResponse, self).__init__()
        self._a_shop_id = None
        self._item_list = None
        self._total = None

    @property
    def a_shop_id(self):
        return self._a_shop_id

    @a_shop_id.setter
    def a_shop_id(self, value):
        self._a_shop_id = value
    @property
    def item_list(self):
        return self._item_list

    @item_list.setter
    def item_list(self, value):
        if isinstance(value, list):
            self._item_list = list()
            for i in value:
                if isinstance(i, AShopItemVO):
                    self._item_list.append(i)
                else:
                    self._item_list.append(AShopItemVO.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppUnishopItemlistQueryResponse, self).parse_response_content(response_content)
        if 'a_shop_id' in response:
            self.a_shop_id = response['a_shop_id']
        if 'item_list' in response:
            self.item_list = response['item_list']
        if 'total' in response:
            self.total = response['total']
