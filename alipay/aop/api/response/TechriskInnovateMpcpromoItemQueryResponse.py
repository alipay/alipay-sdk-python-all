#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ItemQueryInfo import ItemQueryInfo


class TechriskInnovateMpcpromoItemQueryResponse(AlipayResponse):

    def __init__(self):
        super(TechriskInnovateMpcpromoItemQueryResponse, self).__init__()
        self._item_list = None
        self._recommend_id = None

    @property
    def item_list(self):
        return self._item_list

    @item_list.setter
    def item_list(self, value):
        if isinstance(value, list):
            self._item_list = list()
            for i in value:
                if isinstance(i, ItemQueryInfo):
                    self._item_list.append(i)
                else:
                    self._item_list.append(ItemQueryInfo.from_alipay_dict(i))
    @property
    def recommend_id(self):
        return self._recommend_id

    @recommend_id.setter
    def recommend_id(self, value):
        self._recommend_id = value

    def parse_response_content(self, response_content):
        response = super(TechriskInnovateMpcpromoItemQueryResponse, self).parse_response_content(response_content)
        if 'item_list' in response:
            self.item_list = response['item_list']
        if 'recommend_id' in response:
            self.recommend_id = response['recommend_id']
