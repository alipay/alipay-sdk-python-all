#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppRoomrentDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppRoomrentDeleteResponse, self).__init__()
        self._item_id_list = None
        self._out_item_id_list = None

    @property
    def item_id_list(self):
        return self._item_id_list

    @item_id_list.setter
    def item_id_list(self, value):
        if isinstance(value, list):
            self._item_id_list = list()
            for i in value:
                self._item_id_list.append(i)
    @property
    def out_item_id_list(self):
        return self._out_item_id_list

    @out_item_id_list.setter
    def out_item_id_list(self, value):
        if isinstance(value, list):
            self._out_item_id_list = list()
            for i in value:
                self._out_item_id_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppRoomrentDeleteResponse, self).parse_response_content(response_content)
        if 'item_id_list' in response:
            self.item_id_list = response['item_id_list']
        if 'out_item_id_list' in response:
            self.out_item_id_list = response['out_item_id_list']
