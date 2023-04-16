#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ShopItem import ShopItem


class AlipayOpenMiniCloudAosshopQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniCloudAosshopQueryResponse, self).__init__()
        self._item_total_count = None
        self._result = None
        self._sequence = None

    @property
    def item_total_count(self):
        return self._item_total_count

    @item_total_count.setter
    def item_total_count(self, value):
        self._item_total_count = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, list):
            self._result = list()
            for i in value:
                if isinstance(i, ShopItem):
                    self._result.append(i)
                else:
                    self._result.append(ShopItem.from_alipay_dict(i))
    @property
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, value):
        self._sequence = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniCloudAosshopQueryResponse, self).parse_response_content(response_content)
        if 'item_total_count' in response:
            self.item_total_count = response['item_total_count']
        if 'result' in response:
            self.result = response['result']
        if 'sequence' in response:
            self.sequence = response['sequence']
