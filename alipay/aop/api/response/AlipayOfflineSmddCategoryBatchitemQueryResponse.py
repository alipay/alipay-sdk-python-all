#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ItemBean import ItemBean


class AlipayOfflineSmddCategoryBatchitemQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineSmddCategoryBatchitemQueryResponse, self).__init__()
        self._item_list = None

    @property
    def item_list(self):
        return self._item_list

    @item_list.setter
    def item_list(self, value):
        if isinstance(value, list):
            self._item_list = list()
            for i in value:
                if isinstance(i, ItemBean):
                    self._item_list.append(i)
                else:
                    self._item_list.append(ItemBean.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineSmddCategoryBatchitemQueryResponse, self).parse_response_content(response_content)
        if 'item_list' in response:
            self.item_list = response['item_list']
