#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ItemCardOpenapi import ItemCardOpenapi


class AlipayUserUgshoppingRecommendQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserUgshoppingRecommendQueryResponse, self).__init__()
        self._item_cards = None
        self._next_page_num = None

    @property
    def item_cards(self):
        return self._item_cards

    @item_cards.setter
    def item_cards(self, value):
        if isinstance(value, list):
            self._item_cards = list()
            for i in value:
                if isinstance(i, ItemCardOpenapi):
                    self._item_cards.append(i)
                else:
                    self._item_cards.append(ItemCardOpenapi.from_alipay_dict(i))
    @property
    def next_page_num(self):
        return self._next_page_num

    @next_page_num.setter
    def next_page_num(self, value):
        self._next_page_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserUgshoppingRecommendQueryResponse, self).parse_response_content(response_content)
        if 'item_cards' in response:
            self.item_cards = response['item_cards']
        if 'next_page_num' in response:
            self.next_page_num = response['next_page_num']
