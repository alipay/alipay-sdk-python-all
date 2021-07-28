#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KbdishVirtualDishInfo import KbdishVirtualDishInfo


class KoubeiCateringDishVirtualdishQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringDishVirtualdishQueryResponse, self).__init__()
        self._dish_list = None
        self._shop_id = None

    @property
    def dish_list(self):
        return self._dish_list

    @dish_list.setter
    def dish_list(self, value):
        if isinstance(value, list):
            self._dish_list = list()
            for i in value:
                if isinstance(i, KbdishVirtualDishInfo):
                    self._dish_list.append(i)
                else:
                    self._dish_list.append(KbdishVirtualDishInfo.from_alipay_dict(i))
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringDishVirtualdishQueryResponse, self).parse_response_content(response_content)
        if 'dish_list' in response:
            self.dish_list = response['dish_list']
        if 'shop_id' in response:
            self.shop_id = response['shop_id']
