#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ItemQueryInfo import ItemQueryInfo


class TechriskInnovateMpcpromoItemQueryResponse(AlipayResponse):

    def __init__(self):
        super(TechriskInnovateMpcpromoItemQueryResponse, self).__init__()
        self._item_list = None

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

    def parse_response_content(self, response_content):
        response = super(TechriskInnovateMpcpromoItemQueryResponse, self).parse_response_content(response_content)
        if 'item_list' in response:
            self.item_list = response['item_list']
