#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ItemResp import ItemResp


class KoubeiMarketingDataMallRecommendGetResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingDataMallRecommendGetResponse, self).__init__()
        self._has_more = None
        self._items = None

    @property
    def has_more(self):
        return self._has_more

    @has_more.setter
    def has_more(self, value):
        self._has_more = value
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self._items = list()
            for i in value:
                if isinstance(i, ItemResp):
                    self._items.append(i)
                else:
                    self._items.append(ItemResp.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingDataMallRecommendGetResponse, self).parse_response_content(response_content)
        if 'has_more' in response:
            self.has_more = response['has_more']
        if 'items' in response:
            self.items = response['items']
